def pikachu_attak():
    menu = int(input("1) 전기쇼크 2) 십만볼트 3) 백만볼트 ")
               if menu == 1:
                   print('전기쇼크!')
                    def




class Pokemon():
    def __init__(self, name, ty, hp, pw):
        self.name = name
        self.ty = ty
        self.hp = hp
        self.pw = pw


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
    menu = int(input('1) POKEMON GAME START 2) 나가기 : '))
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
                menu_ingame = int(input('1) 이동하기 2) 쉬기 3) 나가기 :'))
                print()
                if menu_ingame == 1:
                    import random
                    num = random.randint(1,4)
                    if num == 1:
                            print('피카츄가 나타났다!')

                    if num == 2:
                            print('이상해씨가 나타났다!')
                    if num == 3:
                            print('리자몽이 나타났다!')
                    if num == 4:
                            print('주위에 포켓몬이 없다')
                elif menu_ingame == 2:
                    print()
                elif menu_ingame == 3:
                    print("종료하였습니다")







    elif menu == 2:
        print("종료하였습니다")
        break
    else:
        print('choose number 1 or 2')



