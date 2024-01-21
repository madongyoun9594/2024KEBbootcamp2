
class Pokemon():
    def __init__(self, name, ty, hp, pw):
        self.name = name
        self.ty = ty
        self.hp = int(hp)
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


class Pokemon_attak(Pokemon):
    def __init__(self,attack1, attack2, attack1dam, attack2dam):
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack1dam = int(attack1dam)
        self.attack2dam = int(attack2dam)
pa = Pokemon_attak("전기쇼크", '십만볼트','20','35')
ca = Pokemon_attak("화염방사",'용의파동','35','50')
ba = Pokemon_attak("덩쿨채찍","씨폭탄",15,25)



def attackf():
    print()
    if menu == 1:
        print('사용할 기술을 선택하세요')
        print()
        menu_2 = int(input(f'1) {ka.attack1}, 2) {ka.attack2} : '))
        print()
        if menu_2 == 1:
            print(f'{ka.attack1}!!')
            return ka.attack1

        elif menu_2 == 2:
            print(f'{ka.attack2}!!')
            return ka.attack2
def p1enemy_attack():
    import random
    number = random.randint(1,2)
    if number == 1:
        print(f'{p1.name}이(가) {pa.attack1}을 사용하였다!')
        k.hp = k.hp - pa.attack1dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')
    elif number == 2:
        print(f'{p1.name}이(가) {pa.attack2}을 사용하였다')
        k.hp = k.hp - pa.attack2dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')
def c1enemy_attack():
    import random
    number = random.randint(1,2)
    if number == 1:
        print(f'{c1.name}이(가) {ca.attack1}을(를) 사용하였다!')
        k.hp = k.hp - ca.attack1dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')
    elif number == 2:
        print(f'{c1.name}이(가) {pa.attack2}을 사용하였다')
        k.hp = k.hp - ca.attack2dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')
def b1enemy_attack():
    import random
    number = random.randint(1,2)
    if number == 1:
        print(f'{b1.name}이(가) {ba.attack1}을(를) 사용하였다!')
        k.hp = k.hp - ba.attack1dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')
    elif number == 2:
        print(f'{b1.name}이(가) {ba.attack2}을 사용하였다')
        k.hp = k.hp - ba.attack2dam
        print()
        print(f'{k.name}의 남은 체력: {k.hp}')






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
                ka = pa
            elif menu_selection == 2:
                k = c1
                ka = ca

            elif menu_selection == 3:
                k = b1
                ka = ba
            print()
            print(f'이름:{k.name}   속성:{k.ty}   체력:{k.hp}   전투력:{k.pw}')
            print()
            print('무엇을 하시겠습니까? ')
            print()
            while True:
                menu_ingame = int(input('1) 이동하기 2) 쉬기 3) 나가기 :'))
                print()
                if menu_ingame == 1:
                    import random
                    num = random.randint(1,4)
                    if num == 1:
                            print(f'{p1.name}가 나타났다!')
                            print()
                            print(f'{p1.name}의 체력: {p1.hp} {p1.name}의 전투력: {p1.pw}')
                            print()
                            menu = int(input('1) 싸운다 2) 도망간다 :'))
                            while p1.hp > 0 or k.hp > 0:
                                attackf()
                                if ka.attack1:
                                    p1.hp = p1.hp - ka.attack1dam
                                    print(f'{p1.name}의 남은 체력: {p1.hp}')
                                    if p1.hp < 0:
                                        print('승리하였다')
                                        break
                                    if k.hp < 0:
                                        print('패배하였다')
                                        break
                                if ka.attack2:
                                    p1.hp = p1.hp - pa.attack2dam
                                    print(f'{p1.name}의 남은 체력: {p1.hp}')
                                    if p1.hp <0:
                                        print("승리하였다")
                                        break
                                    if k.hp <0:
                                        print('패배하였다')
                                        break
                                p1enemy_attack()
                    if num == 2:
                            print(f'{c1.name}가 나타났다!')
                            print()
                            print(f'{c1.name}의 체력: {c1.hp} {c1.name}의 전투력: {c1.pw}')
                            print()
                            menu = int(input('1) 싸운다 2) 도망간다 :'))
                            while c1.hp > 0 or k.hp > 0:
                                attackf()
                                if ka.attack1:
                                    c1.hp = c1.hp - ka.attack1dam
                                    print(f'{c1.name}의 남은 체력: {c1.hp}')
                                    if c1.hp < 0:
                                        print('승리하였다')
                                        break
                                    if k.hp < 0:
                                        print('패배하였다')
                                        break
                                if ka.attack2:
                                    c1.hp = c1.hp - ca.attack2dam
                                    print(f'{c1.name}의 남은 체력: {c1.hp}')
                                    if c1.hp < 0:
                                        print("승리하였다")
                                        break
                                    if k.hp < 0:
                                        print('패배하였다')
                                        break
                                c1enemy_attack()

                    if num == 3:
                        print(f'{b1.name}가 나타났다!')
                        print()
                        print(f'{b1.name}의 체력: {b1.hp} {b1.name}의 전투력: {b1.pw}')
                        print()
                        menu = int(input('1) 싸운다 2) 도망간다 :'))
                        while b1.hp > 0 or k.hp > 0:
                            attackf()
                            if ka.attack1:
                                b1.hp = b1.hp - ka.attack1dam
                                print(f'{b1.name}의 남은 체력: {b1.hp}')
                                if b1.hp < 0:
                                    print('승리하였다')
                                    break
                                if k.hp < 0:
                                    print('패배하였다')
                                    break
                            if ka.attack2:
                                b1.hp = b1.hp - ba.attack2dam
                                print(f'{b1.name}의 남은 체력: {b1.hp}')
                                if b1.hp < 0:
                                    print("승리하였다")
                                    break
                                if k.hp < 0:
                                    print('패배하였다')
                                    break
                            b1enemy_attack()

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

