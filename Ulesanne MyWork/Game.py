import tkinter as tk
import random

# Глобальные переменные
player_level = 1
player_bonus = 0  # Сила от шмоток
player_hand = []
current_monster = None

treasure_deck = ["Меч +2", "Щит +1", "Зелье +3"]
door_deck = [
    {"name": "Гоблин", "power": 4, "treasures": 1},
    {"name": "Дракон", "power": 10, "treasures": 3},
    {"name": "Проклятие! Потеряй уровень", "curse": True},
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
        card = door_deck.pop(0)

        # Если это монстр, начинается бой
        if "power" in card:
            current_monster = card
            info_label.config(text=f"Монстр: {card['name']} (Сила {card['power']})")
            fight_button.config(state=tk.NORMAL)
            run_button.config(state=tk.NORMAL)
        elif "curse" in card:
            player_level = max(1, player_level - 1)  # Потеря уровня
            info_label.config(text=f"Проклятие! {card['name']}\nУровень: {player_level}")
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
                    player_hand.append(treasure_deck.pop(0))
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

# UI Элементы
info_label = tk.Label(root, text=f"Уровень: {player_level}\nКарты: {player_hand}", font=("Arial", 12))
info_label.pack(pady=20)

# Контейнер для кнопок
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

draw_door_button = tk.Button(button_frame, text="Открыть Дверь", command=draw_door)
draw_door_button.grid(row=0, column=0, padx=5)

fight_button = tk.Button(button_frame, text="Биться с монстром", command=fight, state=tk.DISABLED)
fight_button.grid(row=0, column=1, padx=5)

run_button = tk.Button(button_frame, text="Убежать", command=run_away, state=tk.DISABLED)
run_button.grid(row=0, column=2, padx=5)

end_turn_button = tk.Button(button_frame, text="Конец хода", command=end_turn)
end_turn_button.grid(row=0, column=3, padx=5)

# Запуск игры
root.mainloop()


