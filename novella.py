import random
import time


inventory = []


levels = ("Темный лес", "Заброшенный дом", "Подземный бункер")


items = {
    "Темный лес": ["фонарик", "компас", "записка"],
    "Заброшенный дом": ["ключ", "фотография", "карта"],
    "Подземный бункер": ["противогаз", "шифр", "батарейки"]
}


puzzles = {
    "Темный лес": {"вопрос": "Что растет вверх корнями?", "ответ": "сосулька"},
    "Заброшенный дом": {"вопрос": "Что можно увидеть с закрытыми глазами?", "ответ": "сон"},
    "Подземный бункер": {"вопрос": "Что всегда увеличивается, но никогда не уменьшается?", "ответ": "возраст"}
}


opened_doors = set()


def start_game():
    print("Добро пожаловать в игру 'Побег от Слендермена'!")
    print("Ваша цель - пройти через все уровни и выжить, избегая Слендермена.")
    time.sleep(1.5)
    for level in levels:
        play_level(level)
    print("Поздравляем! Вы прошли все уровни и спаслись от Слендермена!")


def play_level(level):
    print(f"\n=== {level.upper()} ===")
    print(f"Вы находитесь в локации: {level}")
    
    while True:
        action = input("Что вы хотите сделать? (осмотреться/взять/использовать/идти дальше): ").lower()
        
        if action == "осмотреться":
            look_around(level)
        elif action == "взять":
            take_item(level)
        elif action == "использовать":
            use_item(level)
        elif action == "идти дальше":
            if solve_puzzle(level):
                break
            else:
                print("Вы не можете идти дальше, пока не решите загадку!")
        else:
            print("Неизвестное действие. Попробуйте еще раз.")
        
        
        if random.random() < 0.2:
            slenderman_encounter()


def look_around(level):
    print(f"Вы осматриваетесь вокруг. Вы видите следующие предметы:")
    for item in items[level]:
        print(f"- {item}")


def take_item(level):
    item = input("Какой предмет вы хотите взять? ").lower()
    if item in items[level]:
        inventory.append(item)
        items[level].remove(item)
        print(f"Вы взяли {item}. Ваш инвентарь: {inventory}")
    else:
        print("Такого предмета здесь нет.")


def use_item(level):
    item = input("Какой предмет вы хотите использовать? ").lower()
    if item in inventory:
        print(f"Вы использовали {item}.")
        if item == "ключ" and level == "Заброшенный дом":
            opened_doors.add("главная дверь")
            print("Вы открыли главную дверь дома!")
        elif item == "фонарик" and level == "Темный лес":
            print("Вы осветили темный участок леса и нашли тайную тропинку!")
        else:
            print("Этот предмет здесь не пригодился.")
    else:
        print("У вас нет такого предмета в инвентаре.")


def solve_puzzle(level):
    print("Чтобы пройти дальше, вы должны решить загадку:")
    print(puzzles[level]["вопрос"])
    answer = input("Ваш ответ: ").lower()
    if answer == puzzles[level]["ответ"]:
        print("Правильно! Вы можете идти дальше.")
        return True
    else:
        print("Неправильно. Попробуйте еще раз.")
        return False


def slenderman_encounter():
    print("\nВНИМАНИЕ! Слендермен появился поблизости!")
    action = input("Что вы будете делать? (бежать/прятаться): ").lower()
    if action == "бежать":
        if random.random() < 0.5:
            print("Вам удалось убежать от Слендермена!")
        else:
            print("Слендермен догнал вас. Игра окончена.")
            exit()
    elif action == "прятаться":
        if random.random() < 0.7:
            print("Вы успешно спрятались, и Слендермен прошел мимо.")
        else:
            print("Слендермен нашел вас. Игра окончена.")
            exit()
    else:
        print("Пока вы медлили, Слендермен настиг вас. Игра окончена.")
        exit()


if __name__ == "__main__":
    start_game()