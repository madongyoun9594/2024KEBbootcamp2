number = int(input('Enter a number: '))

i = 2
while i < number:
        if number % i == 0:
            print(f'{number} is not prime')
            break
        i += 1
if i == number:
    print(f'The number {number} is prime')


