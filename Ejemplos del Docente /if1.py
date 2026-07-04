"""
> >=
< <=
==
!=
and
or

edad = int(input('ingrese su edad:'))
if (edad>=18):
    print('es  mayor')
else:

menor = 1
mayor = 100
numero = int(input('Ingrese un numero:'))
if (numero >= menor) and (numero<=mayor):
    print('esta dentro del rango')
else:
    print('fuera de rango')
    print('es menor')
"""
user = 'admin'
passw = 'admin'
us = input('Username:')
ps = input('Password:')
if (user==us)or(passw==ps):
    print('bienvenido al sistema')
else:
    print('usuario y/o contraseña incorrectos')
