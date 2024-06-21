### EJERCICIO 05.

edad = int(input("Por favor, ingresa la edad del cliente: "))


if edad < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad <= 18:
    precio_entrada = 10  # Clientes de 4 a 18 años pagan 10 soles
else:
    precio_entrada = 20  # Clientes mayores de 18 años 
print(f"El precio de la entrada para el cliente de {edad} años es: {precio_entrada} soles.")