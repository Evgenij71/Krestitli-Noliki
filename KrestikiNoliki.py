pole = [['', '' , ''],
        ['', '' , ''],
        ['', '' , '']]


def pokaz_polе(q):
    print(' 0 1 2')
    for i in range(len(pole)):
       print(str(i),*pole[i])

pokaz_polе(pole)


def game_input(q):
    while True:
        place= input('координаты:').split()
        if len(place) !=2:
            print('введите только 2 координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('только цифры')
            continue
        x,y=map (int,place)
        if not (x >= 0 and x < 3 and y < 3):
            print('неверное значение')
            continue
        if q[x][y] != '':
            print('клетка уже занята')

        break
    return x,y

game_input(pole)


def win_p(q,player):
    def check_line(a1,a2,a3,palyer):
        if a1==player and a2 == player and a3 == player:
            return True

    for n in range(3):
        if check_line(q[n][0],q[n][1],q[n][2],player) or check_line(q[0][n],q[1][n],q[2][n],player) or check_line(q[0][0],q[1][1],q[2][2],player):
            return True

    return False

pole=[['']*3 for _ in range(3)]
c= 0
while True:
    if c%2==0 or c==0:
        player='X'
    else:
        player='O'

    pokaz_polе(pole)
    x,y=game_input(pole)
    pole[x][y]=player
    if c==9:
        print('ничья')
    if  win_p(pole,player):
        print('победа')
        break

    c+=1





