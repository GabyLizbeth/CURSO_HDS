### EJERCICIO 04.

Nombre = input("¿Cual es tu nombre")
Genero = input("¿Cual es tu genero (M o F)?")
if Genero == "M":
    if Nombre.lower() <"m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if Nombre.lower() >"n":
        grupo = "A"
    else:
        grupo = "B"
print("Al grupo que perteneces es " + grupo)