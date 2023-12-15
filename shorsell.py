def Shellsort(arr):
    n = len(arr)
    intervalo = n // 2

    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i
            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo
            arr[j] = temp

        intervalo //= 2


MiLista = [0, 2, 5, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Shellsort(MiLista)
print("Lista ordenada:", MiLista)
