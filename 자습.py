# class Thing2():
#     def __init__(self,letters):
#         self.letters = letters
#
# k = Thing2('abc')
#
# print(k.letters)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.number = number
        self.symbol =symbol
    def dump(self):
        print(f'name: {self.name}, number: {self.number}, symbol: {self.symbol}')

el_dict = dict(name='Hydrogen', symbol='H', number=1)

hydrogen_is = Element(**el_dict)


hydrogen_is.dump()
























