
e2f = dict(dog='chien', cat='chat', walrus='mors')
f2e = {}
for (영어, 프랑스어) in e2f.items():
    f2e[프랑스어] = 영어
while True:
    menu = input( '1) e2f dict  2) f2e dict  3) quit : ')
    if menu == '1':
        E = input('영어: ')
        print(f'프랑스어: {e2f.get(E)} ')
    elif menu == '2':
        F = input('프랑스어: ')
        print(f'영어: {f2e.get(F)} ')
    elif menu == '3':
        print("종료")
        break
    else:
        print('재입력')

