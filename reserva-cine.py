asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

3
fila = int(input("Ingrese la fila del asiento (1-3): "))
columna = int(input("Ingrese la columna del asiento (1-4): "))


fila = fila - 1
columna = columna - 1

asientos[fila][columna] = 1

print("\nEstado de los asientos:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
