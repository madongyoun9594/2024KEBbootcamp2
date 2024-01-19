class Pokemon():
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")


class Pikachu(Pokemon):  # is-⍺
    def __init__(self, name, type):
        self.type = type
        self.name = name
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")
class Squirtle(Pokemon):
    pass

p1 = Pikachu("피카츄",'전기')
p2 = Squirtle("꼬부기")
p3 = Pokemon("아무개")
p1.attack(p2)

