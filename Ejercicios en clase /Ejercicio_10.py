'''
Factorial de un numero
'''
num = int(input('ingrese un numero para saber su factorial'))
fac = 1 

for x in range (1, num+1):
    x = fac * x
    print('el factorial de ',num,'es de ',x)
    