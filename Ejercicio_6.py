edad = int(input('Ingrese su peso'))

if (edad >= 0) and (edad <= 10):
    print('bajo peso')
elif (edad >= 11) and (edad <= 20) :
    print('peso normal')
elif (edad >= 21) and (edad <= 60):
    print('sobre peso')
elif (edad >= 60) and (edad <= 100):
    print('obesidad')
else:
    print('peso incorrecto')