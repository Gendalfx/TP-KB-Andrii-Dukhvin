import random

choices = ["stone", "scissor", "paper"]

# Запит 
user_choice = input("Виберіть (stone, scissor, paper): ").lower()

# Перевірка на правильність введення
if user_choice not in choices:
    print("Невірний вибір! Будь ласка, виберіть 'stone', 'scissor' або 'paper'")
else:
    # Випадковий вибір комп'ютера
    computer_choice = random.choice(choices)
    print(f"Комп'ютер вибрав: {computer_choice}")

    # Визначення переможця
    if user_choice == computer_choice:
        print("Нічия!")
    elif (user_choice == "stone" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "stone"):
        print("Ви виграли!")
    else:
        print("Комп'ютер виграв!")
