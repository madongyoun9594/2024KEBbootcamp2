# prime number
number = int(input('Enter a number: '))
is_prime = True


if number < 2:
    print(f'{number} is Not a prime number')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i = i + 1
    # print(i, end='')

# if cnt == 0:
if is_prime:  # remove ==
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

