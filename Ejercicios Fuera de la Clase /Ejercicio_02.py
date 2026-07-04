'''
Un depósito de agua tiene capacidad para 1000 litros. 
Solicite la cantidad de litros que desea almacenar un usuario. 
Si la cantidad es menor o igual a la capacidad, indique que el almacenamiento fue exitoso; 
caso contrario, informe que excede la capacidad.
'''

Cantidad = float(input('ingrese la cantida de agua que quiere almacenar en el tanque'))

if(Cantidad <= 1000):
    print('Almacenamieto Exitoso')
else:
    print('lLa cantidad excede la capacidad del tanque.')