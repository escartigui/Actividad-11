def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista[1:] if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

cantidad = int(input("Ingrese la cantidad de personas: "))
if cantidad >= 0:
    for x in range(cantidad):
     nombre = input("Ingrese su nombre: ")

     resultado = quick_sort(nombre)
     print(resultado)

