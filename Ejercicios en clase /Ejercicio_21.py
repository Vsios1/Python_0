user_name = 'admin'
user_pass = 'admin'

intento = 1
while intento <= 3:
    print('   INTENTO NUMERO#',intento)
    name = input('Ingrese su nombre de usuario:')
    passw = input('Ingrese su contraseña:')
    if user_name == name and user_pass==passw:
        print('LOGIN EXITOSO BIENVENIDO')
        while True:
            print("""
            Bien Benido a la Calculadora de Vector el Magnifico Jajajajaja

        1.- SUMAR
        2.- RESTAR
        3.- MULTIPLICAR
        4.- DIVIDIR
        5.- SALIR

    """)
    op =input('Ingrese el numero de su opcion:')
    if op == '1':
        print('.:SUMA:.')
        n1 = int(input('N1:'))
        n2 = int(input('N2:'))
        s = n1 + n2
        print('SUMA:',s)
    elif op == '2':
        print('.:RESTA:.')
        n1 = int(input('N1:'))
        n2 = int(input('N2:'))
        r = n1 - n2
        print('RESTA:',r)
    elif op == '3':
        print('.:MULTIPLICACION:.')
        n1 = int(input('N1:'))
        n2 = int(input('N2:'))
        M = n1 * n2
        print('MULTIPLICACION:',M)
    elif op == '4':
        print('.:DIVISION:.')
        n1 = int(input('N1:'))
        n2 = int(input('N2:'))
        if n2 != 0:
              d = n1/n2
              print('DIVISION:',d)
        else:
            print('error no se puede dividir entre 0')
    elif op == '5':
        print('GRACIAS POR UTILIZAR MI CALCULADORA...')
        break
    else:
        print('OPCION NO VALIDA')
    print('Usuario y/o contraseña incorrectos')
    intento = intento +1
    