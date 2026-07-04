cadena = input("Ingrese una frase: ")
newP = ""

for char in cadena:
    if char == " ":
        newP = newP + "_"
    else:
        newP = newP + char

print(newP)