def Metodo_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenar_numeros(archivo, archivo_ordenado):
    #extraer numeros del archivo:
    with open(archivo, 'r') as f:
        numeros = [int(num) for num in f.readlines()]
    #ordenar mumero por burbuja:
    numeros_ordenados = Metodo_burbuja(numeros)
    #escribir numeros ordenados en el otro archivo:
    with open(archivo_ordenado, 'w') as f:
        for n in numeros_ordenados:
            f.write(str(n) + '\n')
    print("Se han ordenados los numeros del archivo")

# Ejemplo de uso
ordenar_numeros('numeros.txt', 'ordenados.txt')