# prime number
numbers = input("Input first second number : ").split()
n1=int(numbers[0])
n2=int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        # pass
        continue

    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
# 화씨 섭씨 3번메뉴 소수 판정 프로그램 4번 메뉴 구간 소수 프로그램
# 연습문제 143쪽  1,2,3 깃허브




#         i = i + 1
# print()
#
#     if is_prime:
#         print(f'{number} is prime number')
#     else:
#         print(f'{number} is NOT prime number!')
# for letter in univ:
#     print(letter, end=' ')
#
# print()
#
# #for k in range(0, len(univ), 1):
# #for k in range(0, len(univ)):
# for k in range(len(univ)):
#     print(univ[k], end=' ')