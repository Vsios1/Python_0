"""
Se debe crear un login de cuenta de usuario
    user:
    pass:
si los datos son correctos se dara acceso al sistema
sino se le dara maximo 3 intentos para el login

"""
user_name = 'admin'
user_pass = 'admin'

intento = 1
while intento <= 3:
    print('   INTENTO NUMERO#',intento)
    name = input('Ingrese su nombre de usuario:')
    passw = input('Ingrese su contraseña:')
    if user_name == name and user_pass==passw:
        print('LOGIN EXITOSO BIENVENIDO')
        break
    print('Usuario y/o contraseña incorrectos')
    intento = intento +1
    
        
