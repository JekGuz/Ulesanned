import tkinter as tk
import random
from PIL import Image, ImageTk

# Глобальные переменные
player_level = 1
player_bonus = 0  # Сила от шмоток
player_hand = []  # Что у игра в рук
current_monster = None

treasure_deck = ["Меч +2", "Щит +1", "Зелье +3", "броник +1", "Бензопила +2", "Шлем-Рогач +1", "Башмаки Могучего Пенделя +2", "Хотельное кольцо +1", "Крыса на полочке +0", "Коленеотбойный Молоточек +4"]
door_deck = [
    {"name": "Гоблин", "power": 4, "treasures": 2},
    {"name": "Пасюк с Кувалдой", "power": 1, "treasures": 1},
    {"name": "Типа вошки", "power": 1, "treasures": 1},
    {"name": "Лятучие Легишки", "power": 2, "treasures": 1},
    {"name": "Здоровенная Бешеная Цыпа", "power": 2, "treasures": 1},
    {"name": "Неживой Коник", "power": 3, "treasures": 2},
    {"name": "Сопливый нос", "power": 5, "treasures": 3},

    {"name": "Проклятие! Потеряй уровень", "curse": True},
    {"name": "Получи уровень", "levelUP": True},

    {"name": "Класс: Воин", "type": "class"},
    {"name": "Класс: Маг", "type": "class"},
    {"name": "Класс: Эльф", "type": "class"},
    {"name": "Класс: Клирик", "type": "class"},
    {"name": "Класс: Вор", "type": "class"}
]

random.shuffle(door_deck)
random.shuffle(treasure_deck)

# Функция обновления интерфейса
def update_ui():
    info_label.config(text=f"Уровень: {player_level}\nКарты: {', '.join(player_hand)}")

# Функция для открытия двери
def draw_door():
    global current_monster, player_level

    if door_deck:
        card = random.choice(door_deck)

        # Если это монстр, начинается бой
        if "power" in card:
            current_monster = card
            info_label.config(text=f"Монстр: {card['name']} (Сила {card['power']})")
            fight_button.config(state=tk.NORMAL)
            run_button.config(state=tk.NORMAL)
        elif "curse" in card:
            player_level = max(1, player_level - 1)  # Потеря уровня
            info_label.config(text=f"Проклятие! {card['name']}\nУровень: {player_level}")
        elif "levelUP" in card:
            player_level = max(1, player_level + 1)  # Получи уровень
            info_label.config(text=f"Получи уровень! {card['name']}\nУровень: {player_level}")
        else:
            player_hand.append(card["name"])  # Обычная карта в руку
            update_ui()

# Функция для боя
def fight():
    global current_monster, player_level

    if current_monster:
        player_power = player_level + player_bonus
        monster_power = current_monster["power"]

        if player_power >= monster_power:
            player_level += 1
            for _ in range(current_monster["treasures"]):
                if treasure_deck:
                    player_hand.append(treasure_deck[0])
            info_label.config(text=f"Ты победил! Новый уровень: {player_level}\nКарты: {', '.join(player_hand)}")
        else:
            info_label.config(text="Ты проиграл! Пробуй убежать!")

        current_monster = None
        fight_button.config(state=tk.DISABLED)

# Функция для побега
def run_away():
    global player_level
    roll = random.randint(1, 6)

    if roll >= 5:
        info_label.config(text="Ты убежал!")
    else:
        info_label.config(text="Тебя поймали! Потеряй 1 уровень")
        player_level = max(1, player_level - 1)

    run_button.config(state=tk.DISABLED)
    fight_button.config(state=tk.DISABLED)

# Функция для завершения хода
def end_turn():
    info_label.config(text="Конец хода! Ждем следующего игрока.")


# Создание основного окна
root = tk.Tk()
root.title("Манчкин на Python")
root.geometry("800x600")

# Добавляем картинку (фон)
original_pilt = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\Ulesanne MyWork\wood.jpg")
resize_pilt = original_pilt.resize((800, 600))
bgpilt = ImageTk.PhotoImage(resize_pilt)

# Устанавливаем фон
labelBg = tk.Label(root, image=bgpilt)
labelBg.place(x=0, y=0, relwidth=1, relheight=1)

# Пример надписи поверх фона
label = tk.Label(root, text="Добро пожаловать в Манчкин!", font=("Arial", 16), bg="#ffffff")
label.pack(pady=20)

# UI Элементы
info_label = tk.Label(root, text=f"Уровень: {player_level}\nКарты: {player_hand}", font=("Arial", 12))
info_label.pack(pady=20)

# Контейнер для кнопок
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

tk.Button(button_frame, text="Открыть Дверь", command=draw_door).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Биться с монстром", command=fight, state=tk.DISABLED).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Убежать", command=run_away, state=tk.DISABLED).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Конец хода", command=end_turn).grid(row=0, column=3, padx=5)

# Запуск игры
root.mainloop()


