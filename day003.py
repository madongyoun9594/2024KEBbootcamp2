# prime number
number = int(input('Enter a number: '))
cnt =0
i = 2
while i < number:
    if number % i == 0:
        cnt = cnt + 1
    i = i + 1

if cnt == 0:
            print(f'{number} is prime number')
else:
            print(f'{number} is NOT prime number')


# subjects = {'python': 'kim', 'c++': 'sung', 'datastructures': 'kim', 'database': 'kang'}
# print("{0[python]} {0[datastructures]}".format(subjects))
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())

