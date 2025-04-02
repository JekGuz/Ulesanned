# Добавить индекатор для понимания победим ли мы монстра или нет
# Сохраниение в файле отдельным, чтобы можно было бы вернуться к своему персонажу

import random
from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, Frame, DISABLED, NORMAL, messagebox
import unicodedata
import os
# import sys # Делала exe

# Глобальные переменные
player_level = 1
player_bonus = 0
player_hand = []
current_monster = None
player_class = None


equipped = {
    "weapon": None,
    "armor": None,
    "helmet": None
}

treasure_deck = [
    "Меч +2", "Щит +4", "Зелье +2", "броник +3", "Кинжал +3",
    "Головняк +3", "Башмаки +2", "Кий +1",
    "Крыса +1", "Молот +4"
]


# Это список/лист в нем словарь!
door_deck = [
    {"name": "Молотая крысотка", "power": 1, "treasures": 1},
    {"name": "Типа вошки", "power": 1, "treasures": 1},
    {"name": "Лятучие Лягушки", "power": 2, "treasures": 1},
    {"name": "Питбуль", "power": 2, "treasures": 1},
    {"name": "Сердитый Бройлер", "power": 2, "treasures": 1},
    {"name": "Конь Андедный", "power": 3, "treasures": 2},
    {"name": "Леприкон", "power": 4, "treasures": 2},
    {"name": "Гарпистки", "power": 4, "treasures": 2},
    {"name": "Утконтикора", "power": 6, "treasures": 2},

    {"name": "Проклятие! Потеряй уровень", "curse": True},
    {"name": "Получи уровень", "levelUP": True},

    {"name": "Класс Воин", "type": "class"},
    {"name": "Класс Маг", "type": "class"},
    {"name": "Класс Эльф", "type": "class"},
    {"name": "Класс Клирик", "type": "class"},
    {"name": "Класс Вор", "type": "class"}
]

random.shuffle(door_deck)
random.shuffle(treasure_deck)



# Функция отображения изображения карты
def normalize_card_name(card_name):
     # Удалим спецсимволы и переведем в нормальную форму
    name = unicodedata.normalize("NFKD", card_name)  # "NFKD" — это один из четырёх вариантов нормализации
    name = name.lower().replace(" ", "_")
    name = ''.join(c for c in name if c.isalnum() or c in "_")
    return name

# Функция отображения изображения карты
def show_card_image(card_name):
    try:
        normalized_name = normalize_card_name(card_name)
        filename = f"{normalized_name}.png" # Файл в той же папке

        # Проверяю картинки на читаемость / очень долго искала от куда и куда т.к.
        print(f"Загружаем картинку: {filename}")
        print("Существует ли?", os.path.exists(filename))
        print("Текущая папка:", os.getcwd())


        if not os.path.exists(filename):
            raise FileNotFoundError
        img = Image.open(filename).resize((200, 300))
        img_tk = ImageTk.PhotoImage(img)
        card_image_label.config(image=img_tk, text="")
        card_image_label.image = img_tk
    except:
        card_image_label.image = None
        card_image_label.config(image="", text="(нет изображения)")

# Выбираем что у нас за предмет в соровищах (определяет предмет по ключевым словам)
def get_item_type(item_name):
    item_name = item_name.lower()
    if "меч" in item_name or "кийн" in item_name or "кинжал" in item_name or "молот" in item_name or "крыса" in item_name:
        return "weapon"
    elif "броник" in item_name or "щит" in item_name:
        return "armor"
    elif "головняк" in item_name:
        return "helmet"
    return None

# Обновление информации (визуальную инфо уровень, класс, карты в руке, экипировка)
def update_ui():
    class_text = player_class if player_class else "Человек"
     # Убираем класс из сокровищ
    treasures_only = [card for card in player_hand if card != player_class]
    treasures_text = ', '.join(treasures_only) if treasures_only else "—"
    # Обновление верхней информации
    info_label.config(
        text=f"Уровень: {player_level}"
             f"{f'\nКласс: {player_class}' if player_class else ''}"
             f"\nКарты: {', '.join(player_hand)}"
    )
    # Обновление нижней панели игрока
    equipment_text = ", ".join(f"{slot}: {item}" for slot, item in equipped.items() if item)
    if equipment_text:
        info_label.config(text=info_label.cget("text") + f"\nСнаряжение: {equipment_text}")
    player_status_label.config(
        text=f"◊ Уровень: {player_level}   |   🛡 Класс: {class_text}   |   💼 Сокровища: {treasures_text}"
    )

# Открытие двери
def draw_door():
    global current_monster, player_level, player_class
    if door_deck:
        card = random.choice(door_deck)
        if "power" in card:
            show_card_image(card["name"])
            current_monster = card

            # Подсчёт силы игрока (уровень + бонус)
            player_power = player_level + player_bonus
            monster_power = card["power"]

            # Меняем цвет рамки в зависимости от исхода боя тоесть прописываю зеленую больше или равно, в другом случаи красная
            if player_power > monster_power or player_power == monster_power:
                card_frame.config(highlightbackground="green") # опачки (для себя написала, а оно работает)
            else:
                card_frame.config(highlightbackground="red")

            # Старая часть, оставляем
            info_label.config(text=f"Монстр: {card['name']} (Сила {card['power']})") 
            fight_button.config(state=NORMAL)
            run_button.config(state=NORMAL)
            info_label.config(text=f"Монстр: {card['name']} (Сила {card['power']})")
            fight_button.config(state=NORMAL)
            run_button.config(state=NORMAL)
        elif "curse" in card:
            show_card_image(card["name"])
            player_level = max(1, player_level - 1)
            info_label.config(text=f"Проклятие! {card['name']}\nУровень: {player_level}")
        elif "levelUP" in card:
            show_card_image(card["name"])
            player_level += 1
            info_label.config(text=f"Получи уровень! {card['name']}\nУровень: {player_level}")
            player_level = max(1, player_level + 1) # сегодня добавила увеличить уровень
        elif card.get("type") == "class":
            show_card_image(card["name"])
            if player_class:
                answer = messagebox.askyesno(
                    "Новый класс",
                    f"У тебя уже есть класс: {player_class}.\nЗаменить на {card['name']}?"
                )
                if answer:
                    if player_class in player_hand:
                        player_hand.remove(player_class)
                    player_class = card["name"]
                    player_hand.append(card["name"])
                    update_ui()
                else:
                    info_label.config(text=f"Ты оставил себе прежний класс: {player_class}")
            else:
                player_class = card["name"]
                player_hand.append(card["name"])
                update_ui()
        else:
            show_card_image(card["name"])
            player_hand.append(card["name"])
            update_ui()

# Бой
def fight():
    global current_monster, player_level
    if current_monster:
        player_power = player_level + player_bonus
        monster_power = current_monster["power"]
        if player_power >= monster_power:
            player_level += 1
            for _ in range(current_monster["treasures"]):
                if treasure_deck:
                    card = random.choice(treasure_deck)
                    item_type = get_item_type(card)
                    if item_type and equipped[item_type]:
                        answer = messagebox.askyesno(   # askyesno - yes or no messegebox
                            "Новая экипировка",
                            f"У тебя уже есть {item_type}: {equipped[item_type]}\nЗаменить на {card}?"
                        )
                        if answer:
                            player_hand.remove(equipped[item_type])
                            equipped[item_type] = card
                            player_hand.append(card)
                    else:
                        if item_type:
                            equipped[item_type] = card
                        player_hand.append(card)
                    show_card_image(card)
            info_label.config(
                text=f"Ты победил! Новый уровень: {player_level}\nКарты: {', '.join(player_hand)}"
            )
            update_ui()
        else:
            info_label.config(text="Ты проиграл! Пробуй убежать!")
        current_monster = None
        fight_button.config(state=DISABLED)
        # Сброс цвета рамки
        card_frame.config(highlightbackground="#ffffff")

# Убежать
def run_away():
    global player_level
    roll = random.randint(1, 6)
    if roll >= 5:
        info_label.config(text="Ты убежал!")
    else:
        player_level = max(1, player_level - 1)
        info_label.config(text="Тебя поймали! Потеряй 1 уровень")
    run_button.config(state=DISABLED)
    fight_button.config(state=DISABLED)
    # Сброс цвета рамки
    card_frame.config(highlightbackground="#ffffff")

# Конец хода (сбрасывает все показатили)
def end_turn():
    global player_level, player_bonus, player_hand, player_class, equipped, current_monster
    player_level = 1
    player_bonus = 0
    player_hand = []
    player_class = None
    equipped = {"weapon": None, "armor": None, "helmet": None}
    current_monster = None
    info_label.config(text="Конец хода! Ждем следующего игрока.")
    card_image_label.config(image="", text="")
    update_ui()
    # Сброс цвета рамки
    card_frame.config(highlightbackground="#ffffff")

# Главное окно
root = Tk()
root.title("Манчкин на Python")
root.geometry("800x700")

# Фон
bg_image = Image.open(r"C:\\Users\\kotik\\source\\repos\\Ulesanned\\Ulesanne_MyWork\\wood.jpg")
bg_image = bg_image.resize((800, 700))
bg_photo = ImageTk.PhotoImage(bg_image)
Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# Заголовок
Label(root, text="Добро пожаловать в Манчкин!", font=("Arial", 16), bg="#ffffff").pack(pady=10)

# Информация игрока
info_label = Label(root, text="Уровень: 1\nКарты: []", font=("Arial", 12), bg="#ffffff")
info_label.pack(pady=10)

# Добавляем рамочку белую, которую будем менять
card_frame = Frame(root, bg="#ffffff", highlightthickness=8)
card_frame.pack(pady=10)
card_image_label = Label(card_frame, bg="#ffffff", text="(картинка будет тут)", font=("Arial", 10))
card_image_label.pack()

# Статусы игрока
player_status_label = Label(root, font=("Arial", 11), bg="#ffffff")
player_status_label.pack(pady=5)

# Кнопки
button_frame = Frame(root, bg="#ffffff")
button_frame.pack(pady=10)

draw_door_button = Button(button_frame, text="Открыть Дверь", command=draw_door)
draw_door_button.grid(row=0, column=0, padx=5)

fight_button = Button(button_frame, text="Биться с монстром", command=fight, state=DISABLED)
fight_button.grid(row=0, column=1, padx=5)

run_button = Button(button_frame, text="Убежать", command=run_away, state=DISABLED)
run_button.grid(row=0, column=2, padx=5)

end_turn_button = Button(button_frame, text="Конец хода", command=end_turn)
end_turn_button.grid(row=0, column=3, padx=5)


root.mainloop()