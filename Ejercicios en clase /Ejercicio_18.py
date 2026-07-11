num = int(input('ingrese un numero'))
cont = 0 

while num > 0:
    cont = cont + 1 
    num = num // 10

print('su numero, tiene ',cont,' digitos')
