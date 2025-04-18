def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar si el elemento es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
ordenados = burbuja(numeros)
print("Lista ordenada:", ordenados)
