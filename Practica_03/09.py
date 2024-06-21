### EJERCICIO 09.

frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("LA LETRA", letra , "APARECE", contador, "VECES EN LA FRASE", frase)