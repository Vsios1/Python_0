'''
Solicite al usuario tres números enteros 
y determine cuál es el menor de ellos. 
Si los tres números son iguales, informe dicha situación.
'''

n1 = float(input('Ingrese el primer valor'))
n2 = float(input('Ingrese el segundo valor'))
n3 = float(input('Ingrese el tercer valor'))

if n1 == n2 and n2 == n3:
    print('todo los numeros son iguales,',n1,n2,n3)
if (n1 <= n3) and (n1 <= n2):
    print('el primer valor es el menor, ',n1)
if (n2 <= n1) and (n2 <= n3):
    print('el segundo valor es el menor,',n2)
if (n3 <= n1) and (n3 <= n2):
    print('el tercer numero es el menor, ',n3)

    
