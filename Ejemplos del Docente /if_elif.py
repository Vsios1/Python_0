print('''
CLAcIFICADOR DE EDADES

''')
edad = int(input('Ingrese su edad:'))
if edad>0 and edad<=12:
    print('NIÑO')
elif edad>12 and edad <=17:
    print('ADOLECENTE')
elif edad>17 and edad <=50:
    print('ADULTO')
elif edad>50 and edad<=100:
    print('ADULTO MAYOR')
else:
    print('edad no valida')
