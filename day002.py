base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent  number : '))
print(type(base_number),type(exponent_number))
# print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {base_number**exponent_number}')
print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {pow(base_number,exponent_number)}')

# c like
print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number,exponent_number))),


# money = 5,000,000
# print(money)
# # print(type(money)) # tuple
# cash = 5_000_000
# print(cash)
# print(type(cash)) # int
#
# print( 7 / 2)
# print( 7 // 2)
# print( 3 ** 4)