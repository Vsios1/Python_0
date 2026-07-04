nombre = input('Ingrese su nombre:')
salario = float(input('Ingrese su salario:'))

if salario > 7000:
    impuesto =round( salario * 0.15,2)
    total = salario - impuesto
    print(nombre,' tu salario es de:',salario,' y el impuesto a pagar es de:',impuesto)
    print('Tu liquido a recibir es de:',total)
else:
    print(nombre,' no pagara impuesto y tu salario es de:',salario)
