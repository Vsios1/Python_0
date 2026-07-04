peso=float(input('PESO:'))
altura=float(input('ALTURA:'))
imc =peso/(altura**2)
if imc<1.2:
    print(imc,'bajo peso')
elif imc>=1.2 and imc<=1.8:
    print(imc,'normal')
elif imc>1.8 and imc<2.4:
    print(imc,'sobrepeso')
elif imc>=2.4:
    print(imc,'obesidad')
