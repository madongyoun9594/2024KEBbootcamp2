number = [0,1,2,3]
for i in  range(len(number)-1, -1, -1):
   print(number[i], end='')

print()


guess_me = 7
number = 1
while True:
   if number < guess_me:
      print('too low')
   elif number > guess_me:
      print('opps')
   elif number == guess_me:
      print('found it!')
      break
   number += 1


print()


guess_me = 5
for number in range(10):
      if number < guess_me:
         print('too low')
      elif number == guess_me:
         print('found it')
      elif number > guess_me:
         print('opps')
         break


print()


while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime Number  4) 구간설정 소수구하기  5) quit: ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input('Enter a number: '))
        is_prime = True

        if number < 2:
            print('Not a prime number')
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
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
                print(f'{number} is NOT prime number!')
                # pass
                continue

            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')
    else:
        print('Terminate Program.')
        break
