import random


class Pokemon():
    def __init__(self, name, ty, hp, pw):
        self.name = name
        self.ty = ty
        self.hp = hp
        self.pw = pw
    def attack(self):
        menu_at = input("1) 약한공격 2) 필살기 ")
        if menu_at =='1':
            print(f"[]의 hp를 [] 깍았다.")
        if menu_at =='2':
            print(f"[]의 hp를 [] 깍았다")

class Pikachu(Pokemon):
    pass
class Charmander(Pokemon):
    pass
class Bulbasaur(Pokemon):
    pass

p1 = Pikachu('피카츄',"전기","100",'100')
c1 = Charmander('리자몽','불','140','120')
b1 = Bulbasaur("이상해씨",'풀','120','70')


while True:
    menu = int(input('1) POKEMON GAME START 2) QUIT : '))
    print()
    if menu == 1:
        print('환영합니다')
        print()
        print('포켓몬을 한마리 고르세요.')
        print()
        while True:
            menu_selection = int(input('1) 피카츄 2) 리자몽 3) 이상해씨 : '))
            if menu_selection == 1:
                k = p1
            elif menu_selection == 2:
                k = c1
            elif menu_selection == 3:
                k = b1
            print()
            print(f'이름:{k.name}   속성:{k.ty}   체력:{k.hp}   전투력:{k.pw}')
            print()
            print('무엇을 하시겠습니까? ')
            while True:
                menu_ingame = int(input('1) 싸우기 :'))
                if menu_ingame == 1:
                    import random
                    print(random.randint(1.3))



        input('')
    elif menu == 2:
        print("terminate")
        break
    else:
        print('choose number 1 or 2')



