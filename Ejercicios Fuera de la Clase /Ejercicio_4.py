'''
Solicite al usuario un número
y dos límites (inferior y superior). 
Determine si el número se encuentra:

Dentro del rango.
Exactamente en uno de los límites.
Fuera del rango.
'''

num = float(input('Ingrese un numero'))
Rinf = float(input('Ingrese el rango inferior'))
Rsup = float(input('Ingrese el rango superior'))


if num == Rinf or num == Rsup:
    print('el numero es igual a uno de los dos limites del rango')
if (num > Rinf) and (num < Rsup):
    print('Su numero esta dentro del rango')
else:
    print('Su numero no esta dentro del rango')