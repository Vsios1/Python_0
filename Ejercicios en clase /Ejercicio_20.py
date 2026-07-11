"""Calculadora Python"""

def menu():
    print('''
1. suma
2. resta
3. multiplicacion
4. division
5. salir
''')

while True:
    menu()
    try:
        num = input('Elija que operacion desea realizar: ')
    except ValueError:
        print('Opcion no valida')
        continue

    if num == 1:
        num_1 = float(input('Ingrese el primer numero para sumar: '))
        num_2 = float(input('Ingrese el segundo numero para sumar: '))
        res = num_1 + num_2
        print('El resultado de la suma es:', res)
    elif num == 2:
        num_1 = float(input('Ingrese el primer numero para restar: '))
        num_2 = float(input('Ingrese el segundo numero para restar: '))
        res = num_1 - num_2
        print('El resultado de la resta es:', res)
    elif num == 3:
        num_1 = float(input('Ingrese el primer numero para multiplicar: '))
        num_2 = float(input('Ingrese el segundo numero para multiplicar: '))
        res = num_1 * num_2
        print('El resultado de la multiplicacion es:', res)
    elif num == 4:
        num_1 = float(input('Ingrese el primer numero para dividir: '))
        num_2 = float(input('Ingrese el segundo numero para dividir: '))
        if num_2 == 0:
            print('Error: division por cero')
        else:
            res = num_1 / num_2
            print('El resultado de la division es:', res)
    elif num == 5:
        print('Saliendo...')
        break
    else:
        print('Opcion no valida')

