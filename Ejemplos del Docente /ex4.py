"""
año = int(input('Ingrese un año:'))
if(año %400 == 0)or(año%4==0 and año%100!=0):
    print('True')
else:
    print('False')
"""
n1 = int(input('Ingrese N1:'))
n2 = int(input('Ingrese N2:'))
n3 = int(input('Ingrese N3:'))
mayor = -999999999
if n1>mayor:
    mayor=n1
if n2>mayor:
    mayor=n2
if n3>mayor:
    mayor=n3
print(mayor)

