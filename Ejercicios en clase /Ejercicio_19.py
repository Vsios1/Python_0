num = int(input('ingresa un numero'))
romano = ' '

if num > 1 or num < 999:
    ronUni = num % 10
    num = num //10
    ronDec = num % 10
    num = num //10
    ronCen = num % 10
    num = num //10
    
else:
    print('cantida de digitos incorecto')

'Convercion de Centenas'
if ronCen == 1: 
    romano = romano + 'C'
elif ronCen == 2:
    romano = romano + 'CC'
elif ronCen == 3:
    romano = romano + 'CCC'
elif ronCen == 4:
    romano = romano + 'CD'
elif ronCen == 5:
    romano = romano + 'D'
elif ronCen == 6:
    romano = romano + 'DC'
elif ronCen == 7:
    romano = romano + 'DCC'
elif ronCen == 8:
    romano = romano + 'DCCC'
elif ronCen == 9:
    romano = romano + 'CM'

'Conversion de Decenas'
if ronDec == 1: 
    romano = romano + 'X'
elif ronDec == 2:
    romano = romano + 'XX'
elif ronDec == 3:
    romano = romano + 'XXX'
elif ronDec == 4:
    romano = romano + 'XL'
elif ronDec == 5:
    romano = romano + 'L'
elif ronDec == 6:
    romano = romano + 'LX'
elif ronDec == 7:
    romano = romano + 'LXX'
elif ronDec == 8:
    romano = romano + 'LXXX'
elif ronDec == 9:
    romano = romano + 'XC'

'Conversion de Unidades'
if ronUni == 1: 
    romano = romano + 'I'
elif ronUni == 2:
    romano = romano + 'II'
elif ronUni == 3:
    romano = romano + 'III'
elif ronUni == 4:
    romano = romano + 'IV'
elif ronUni == 5:
    romano = romano + 'V'
elif ronUni == 6:
    romano = romano + 'VI'
elif ronUni == 7:
    romano = romano + 'VII'
elif ronUni == 8:
    romano = romano + 'VII'
elif ronUni == 9:
    romano = romano + 'IX'

print('Su numero original es:',num)
print('Su numero en romanos es: ',romano)



