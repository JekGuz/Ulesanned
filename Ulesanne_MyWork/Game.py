import random
from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, Frame, DISABLED, NORMAL
import unicodedata
import os

# Глобальные переменные
player_level = 1
player_bonus = 0
player_hand = []
current_monster = None

treasure_deck = [
    "Меч +2", "Щит +1", "Зелье +3", "броник +1", "Бензопила +2",
    "Шлем-Рогач +1", "Башмаки Могучего Пенделя +2", "Хотельное кольцо +1",
    "Крыса на полочке +0", "Коленеотбойный Молоточек +4"
]

door_deck = [
    {"name": "Пасюк с Кувалдой", "power": 1, "treasures": 1},
    {"name": "Типа вошки", "power": 1, "treasures": 1},
    {"name": "Питбуль", "power": 1, "treasures": 1},
    {"name": "Лепрокон", "power": 1, "treasures": 1},
    {"name": "Лятучие Легишки", "power": 2, "treasures": 1},
    {"name": "Здоровенная Бешеная Цыпа", "power": 2, "treasures": 1},
    {"name": "Неживой Коник", "power": 3, "treasures": 2},
    {"name": "Гоблин", "power": 4, "treasures": 2},
    {"name": "Сопливый нос", "power": 5, "treasures": 3},

    {"name": "Проклятие! Потеряй уровень", "curse": True},
    {"name": "Получи уровень", "levelUP": True},

    {"name": "Klass Voin", "type": "class"},
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
    name = unicodedata.normalize("NFKD", card_name)
    name = name.lower().replace(" ", "_")
    name = ''.join(c for c in name if c.isalnum() or c in "_")
    return name

def show_card_image(card_name):
    try:
        normalized_name = normalize_card_name(card_name)
        filename = f"{normalized_name}.png"  # Файл в той же папке

        print("Загружаем картинку:", filename)  # проверяем читает ли он названия как я хочу через _

        if not os.path.exists(filename):
            raise FileNotFoundError

        img = Image.open(filename).resize((200, 300))
        img_tk = ImageTk.PhotoImage(img)
        card_image_label.config(image=img_tk, text="")
        card_image_label.image = img_tk  # сохраняем ссылку!
    except:
        card_image_label.config(image="", text="(нет изображения)")
        card_image_label.image = None

# Обновление информации
def update_ui():
    info_label.config(text=f"Уровень: {player_level}\nКарты: {', '.join(player_hand)}")

# Открытие двери
def draw_door():
    global current_monster, player_level

    if door_deck:
        card = random.choice(door_deck)
        show_card_image(card["name"])

        if "power" in card:
            current_monster = card
            info_label.config(text=f"Монстр: {card['name']} (Сила {card['power']})")
            fight_button.config(state=NORMAL)
            run_button.config(state=NORMAL)
        elif "curse" in card:
            player_level = max(1, player_level - 1)
            info_label.config(text=f"Проклятие! {card['name']}\nУровень: {player_level}")
        elif "levelUP" in card:
            player_level += 1
            info_label.config(text=f"Получи уровень! {card['name']}\nУровень: {player_level}")
        else:
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
                    player_hand.append(card)
                    show_card_image(card)  # показать картинку сокровища
            info_label.config(text=f"Ты победил! Новый уровень: {player_level}\nКарты: {', '.join(player_hand)}")
        else:
            info_label.config(text="Ты проиграл! Пробуй убежать!")

        current_monster = None
        fight_button.config(state=DISABLED)

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

# Конец хода
def end_turn():
    info_label.config(text="Конец хода! Ждем следующего игрока.")
    card_image_label.config(image="", text="")

# Главное окно
root = Tk()
root.title("Манчкин на Python")
root.geometry("800x700")

# Фон
bg_image = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\Ulesanne_MyWork\wood.jpg")
bg_image = bg_image.resize((800, 700))
bg_photo = ImageTk.PhotoImage(bg_image)
Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# Заголовок
Label(root, text="Добро пожаловать в Манчкин!", font=("Arial", 16), bg="#ffffff").pack(pady=10)

# Информация игрока
info_label = Label(root, text="Уровень: 1\nКарты: []", font=("Arial", 12), bg="#ffffff")
info_label.pack(pady=10)

# Показ изображения карты
card_image_label = Label(root, bg="#ffffff", text="(картинка будет тут)", font=("Arial", 10))
card_image_label.pack(pady=10)

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

# Старт игры
root.mainloop()
