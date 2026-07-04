print("""
    CAJERO AUTOMATICO

[I]ngreso de dinero
[R]etiros
[S]aldo
""")
cta = 50000
op = input('Ingrese la letra de su opcion:').upper()
if op=='I':
    print('Deposito de dinero')
    monto = float(input('Ingrese un monto:'))
    if monto >0:
        cta = cta + monto
        print('Deposito con exito Saldo:',cta)
    else:
        print('no puede ingresar montos negativos')
elif op=='R':
    print('RETIRO DE DINERO')
    monto = float(input('Ingrese un monto:'))
    if monto<=cta:
        cta = cta-monto
        print('Retiro con exito Saldo:',cta)
    else:
        print('saldo insuficiente')
elif op=='S':
    print('SALDO EN SU CUENTA:',cta)
else:
    print('opcion no valida')
    
"""
string->
cadena.upper()
cadena.lower()
"""
