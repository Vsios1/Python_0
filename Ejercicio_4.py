'Parte 1 '

eyes = int(input('ingrese un año'))

if (eyes / 400 == 0):
    print('no es bisiesto el año')
else:
    if (eyes / 4 == 0):
        if (eyes / 100 == 0 ):
            print ( 'es bisiesto')

'Parte 2'

n1 , n2 , n3 = input('ingrese el primer numero') , input('ingrese el segundo numero') , input('ingrese el tercer numero')
if (n1 > n2 ) and (n1 >n3): 
   print(n1,'este nunero es el mayor')
else: 
   if (n2 > n1 ) and (n2 > n3 ):
      print (n2,'este nunero es el mayor')
   else: 
      if (n3 > n1 ) and (n3 > n2):
         print (n3,'este el mayor')
      else:
         print('Fin del Programa')
         