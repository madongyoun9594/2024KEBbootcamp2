univ = "inha"
i = 0
while i < len(univ):
    print(univ[i], end=' ')
    i = i + 1
# prime number
number = int(input("Input number : "))
is_prime = True

print()
if number < 2:
    print(f'{number} is NOT prime number!')
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

for letter in univ:
    print(letter, end=' ')

print()

#for k in range(0, len(univ), 1):
#for k in range(0, len(univ)):
for k in range(len(univ)):
    print(univ[k], end=' ')
    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number!')

