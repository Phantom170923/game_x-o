
# Функция, где вся основа игры
def game(db):
    maps = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']

    # Инициализация победных линий
    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

    while '-' in maps:
        print_maps(maps)
        while True:
            player_1 = input('Player 1 (x) введите координаты через пробел - ')
            coor = work_maps(player_1)

            if int(coor) in db:
                print('Данное значение уже занято')
            else:
                db.append(coor)
                break
        for i in range(len(maps)):
            maps[int(coor)] = 'x'

        print_maps(maps)

        if '-' not in maps:
            print('Ничья!')
            break

        while True:
            player_2 = input('Player 2 (o) введите координаты через пробел - ')
            coor = work_maps(player_2)
            if int(coor) in db:
                print('Данное значение уже занято')
            else:
                db.append(int(coor))
                break
        for i in range(len(maps)):
            maps[int(coor)] = 'o'

        print_maps(maps)

        if '-' not in maps:
            print('Ничья!')
            break

        if result():
            print(result())
            break


# Функция, которая проверяет выигрыш кого-либо из игроков
def result(maps, victories):
    for i in victories:
        if maps[i[0]] == 'x' and maps[i[1]] == 'x' and maps[i[2]] == 'x':
            return 'win player 1!'
        if maps[i[0]] == 'o' and maps[i[1]] == 'o' and maps[i[2]] == 'o':
            return 'win player 2!'


# Функция, которая преобразовывает введеные пользователем координаты в цифру на поле
def work_maps(player):
    if player == '0 0':
        cor = 0
        return cor
    elif player == '0 1':
        cor = 1
        return cor
    elif player == '0 2':
        cor = 2
        return cor
    elif player == '1 0':
        cor = 3
        return cor
    elif player == '1 1':
        cor = 4
        return cor
    elif player == '1 2':
        cor = 5
        return cor
    elif player == '2 0':
        cor = 6
        return cor
    elif player == '2 1':
        cor = 7
        return cor
    elif player == '2 2':
        cor = 8
        return cor


# Вывод карты на экран
def print_maps(maps):
    print(" ", 0, 1, 2)
    print(0, end=" ")
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(1, end=" ")
    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(2, end=" ")
    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


game(db=list())
