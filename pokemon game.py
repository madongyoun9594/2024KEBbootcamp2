
while True:
    menu = int(input('1) POKEMON GAME START 2) QUIT : '))
    if menu == 1:
        print('welcome to POKEMON GAME')
        break
    elif menu == 2:
        print("terminate")
        break
    else:
        print('choose number 1 or 2')


class Pokemon():
    def __init__(self, name, pt, hp, pw)
        self.name = name
        self.pt = pt
        self.hp = hp
        self.pw = pw