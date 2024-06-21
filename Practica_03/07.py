### EJERCICIO 07.

N = int(input("Escribe la altura del triangulo: "))
for i in range (N):
    for j in range(i+1):
        print("&", end = "")
    print("")