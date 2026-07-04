cadena='       Programacion deSde 0     '
"""
METODOS
.upper()->MAYUSCULAS
.lower()->MINUSCULAS
.strip()->quitar espacios en blanco ini y fin
.lstrip()->izq
.rstrip()->der
.capitalize()->
"""
print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena.lstrip())
print(cadena.rstrip())
print(cadena.capitalize())
print(cadena.title())
print(cadena.split())
print(cadena.replace('Programacion','cero'))

nombre = 'alexis herrera'
print(nombre[1])
print(nombre.replace(' ','_'))
print(nombre[0])
#len()->devuelve la cantidad total de elementos
longitud = len(nombre)
print('La variable nombre tiene un total de:',longitud)
"""
opc condicionales
in
not in
"""
var ='saludos adios'
if 'ad' in var:
    print('true')
else:
    print('false')
if 'AX' not in var:
    print('no esta')
else:
    print('si esta')
