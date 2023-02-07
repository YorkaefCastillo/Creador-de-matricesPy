#Ejercicio práctico #13 (Crear una matriz desde teclado)
x = ""
N = "Matrices"

print(f"{x.center(15,'✨')}")
print(f"{N.center(30)}")
print(f"{x.center(15,'✨')}")


filas = int(input("¿Cuantas filas tendrá la matriz?: "))
columnas = int(input("¿Cuantas columnas  tendrá la matriz?: "))

matriz = []
for posicion_filas in range (filas):
    filas = []
    for elemento in range(columnas): 
        filas.append(input(f"Introduce un elemento a la fila {posicion_filas}:"))
    matriz.append(filas)    

    

for row in matriz:
    print(row)
