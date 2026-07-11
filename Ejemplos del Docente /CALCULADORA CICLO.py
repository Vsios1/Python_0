"""
PARA CADA OPERACION SE PEDIRA SOLO 2 NUMEROS
ADEMAS SE DE CONTROLAR EL ERROR DE LA DIVICION
    NOTA: N/0->ERROR
SI EL USUARIO COLOCA OTRA OPCION MANDAR EL MENSAJE DE OPCION NO VALIDA
        CALCULADORA

    1.- SUMAR
    2.- RESTAR
    3.- MULTIPLICAR
    4.- DIVIDIR
    5.- SALIR

"""
while True:
    print("""
            CALCULADORA

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
