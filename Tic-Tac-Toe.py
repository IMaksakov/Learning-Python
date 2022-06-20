def greetings():
    print("Сегодня играем в крестики-нолики")
    print("         Правила просты         ")
    print("    Вводите 2 координаты хода   ")
    print(" Побеждает игрок, занявший либо:")
    print("--------------------------------")
    print("      --- любую горизонталь     ")
    print("--------------------------------")
    print("       |                        ")
    print("       |любую вертикаль         ")
    print("       |                        ")
    print("--------------------------------")
    print("        /                       ")
    print("       /любую диагональ         ")
    print("      /                         ")
    print("-----------Начинаем-------------")

def show_game_field():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(game_field[i])
        print(f"{i} {row_info}")

def input_request():
    while True:
        coordinates = input("Введите через пробел 2 координаты в формате х = вертикальная ось, y = горизонтальная ось: ").split()
        x, y = coordinates
        x, y = int(x), int(y)
        if 0 > x or x > 2 or  0 > y or  y > 2:
            print("Проверьте координаты")
            continue
        if game_field[x][y] != " ":
            print("Клетка уже занята")
            continue
        return x, y

def win_check():
    win_condition_string = [
        # 1 вертикаль
        ((0, 0), (0, 1), (0, 2)),
        # 2 вертикаль
        ((1, 0), (1, 1), (1, 2)),
        # 3 вертикаль
        ((2, 0), (2, 1), (2, 2)),
        # 1 горизонталь
        ((0, 0), (1, 0), (2, 0)),
        # 2 горизонталь
        ((0, 1), (1, 1), (2, 1)),
        # 3 горизонталь
        ((0, 2), (1, 2), (2, 2)),
        # диагональ с левого верхнего угла
        ((0, 0), (1, 1), (2, 2)),
        # диагональ с левого нижнего угла
        ((2, 0), (1, 1), (0, 2))
    ]

    for i in list(win_condition_string):
        output = []
        for char in i:
            output.append(game_field[char[0]][char[1]])
        if output == ["X", "X", "X"]:
            print("победа за Крестиком")
            return True
        if output == ["0", "0", "0"]:
            print("Победа за Ноликом")
            return True
    return False

# Процесс игры

greetings()
game_field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_game_field()
    if count % 2 == 1:
        print("Ход за крестиком")
    else:
        print("Ход за ноликом")
    x, y = input_request()
    if count % 2 == 1:
        game_field[x][y] = "X"
    else:
        game_field[x][y] = "0"
    if win_check():
        break
    if count == 9:
        print(" Ничья!")
        break