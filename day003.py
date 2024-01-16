# slicing
# print(university[:4])
# print(university[:-11])
# print(len(university))
# print(university[0:len(university)])
# print(university[:16])
# print(university[::2])

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        print('Terminate Program.')
        break
number1 = input("First number : ")
number2 = input("Second number : ")
print(number1 + number2)  # concatenation
print(number1 * 3)  # duplicate
print(number1 + 3)  # TypeError: can only concatenate str (not "int") to str



