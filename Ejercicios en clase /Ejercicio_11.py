num = int(input('Ingrese un nunmero para cuanta vecer se va a iterar'))
incre_par = 0
incre_imp = 0 

for x in range (1, num):
    num_1 = int(input('Ingrese un numero'))
    if (num_1 / 2 == 0 ):
        incre_par = incre_par + 1 
        print('ingresaste esta cantidad de numeros pares, ',incre_par)
    else:
        incre_imp = incre_imp + 1
        print('ingresaste esta cantidad de numeros impares, ',incre_imp)
