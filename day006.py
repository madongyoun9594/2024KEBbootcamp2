class FlyingMixin:
    def fly(self):
        return f"{self.hidden_name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.hidden_name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.hidden_name = name
    def attack(self):
        print("공격!")
    @property
    def name(self):
        return self.hidden_name
    @name.setter
    def name(self, new_name):
        self.hidden_name = new_name

    # name = property(get_name, set_name)
class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("가랴도스")
c1 = Charizard("리자몽")

# print(c1.fly())
# print(g1.swim())
# c1.attack()
# # Charizard.attack()  -> error
# Charizard.attack(c1)
# print(g1.get_name())
# g1.set_name('잉어킹')
# print(g1.name)
print(g1.name)
g1.name = '잉어킹'
print(g1.name)
