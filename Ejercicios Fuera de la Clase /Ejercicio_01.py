'''
Una tienda ofrece un descuento del 10% a los clientes cuya compra sea igual o superior a 500 Bs. 
Solicite el nombre del cliente y el monto de la compra. Muestre el total a pagar.

'''

namen = input('Ingrese su nombre')
Total = float(input('ingrese el Total de su Compra'))

if (Total >= 500):
    Descuento = Total * 0.10
    Td = Total - Descuento
    print('Usted ',namen)
    print('Su descuento es de ',Descuento)
    print('Y su monto total es ',Td)
else:
    print('Usted ',namen)
    print('No acedio el descuento del 10%') 
    print('por lotanto se mantien su monto total que es ',Total)