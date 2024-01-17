
while True:
    menu = input( '1) e2f dict 2) quit : ')
    if menu == '1':
        E = input('영어: ')
        e2f = dict(dog='chien', cat='chat', walrus='mors')
        print(f'프랑스어: {e2f.get(E)} ')
    elif menu == '2':
        print("종료")
        break
    else:
        print('재입력')

