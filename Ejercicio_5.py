edad = int(input('Ingrese su edad'))

if (edad >= 0) and (edad <= 10):
    print('usted es niño')
elif (edad >= 11) and (edad <= 20) :
    print('usted es adolecente')
elif (edad >= 21) and (edad <= 60):
    print('ustede es adulto')
elif (edad >= 60) and (edad <= 100):
    print('usted es persona mayor')