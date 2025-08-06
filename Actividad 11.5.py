Empleados = {}
def quick_sort(listas):
    if len(listas) <= 1:
        return listas
    else:
     pivote = listas[0]
     menores = [x for x in listas[1:] if x < pivote]
     iguales = [x for x in listas[1:] if x == pivote]
     mayores = [x for x in listas[1:] if x > pivote]
     return quick_sort(menores) + iguales + quick_sort(mayores)

def menu():
    while True:
     print("MENU")
     print("1.Agregar")
     print("2.Listado")
     print("3.Salir")
     op = int(input("Ingrese su opción"))
     if op == 1:
        cantidad = int(input("Ingrese la cantidad de elementos: "))
        for i in range(cantidad):
            print(f"Empleado: {i+1}")
            while True:
                Id = int(input("Ingrese ID del empleado: "))
                if Id in Empleados:
                 print("Ya utilizado")
                else:
                 break
            Empleados[Id] = {}
            Empleados[Id]['Nombre'] = input("Ingrese nombre: ")
            Empleados[Id]['Edad'] = int(input("Ingrese edad: "))
            Empleados[Id]['Sexo'] = input("Ingrese sexo: ")
            Empleados[Id]['Ocupación'] = {}
            canti = int(input("Ingrese la cantidad de ocupaciones: "))
            for i in range(canti):
             print(f"Ocupación {i+1}")
             while True:
                 codigo = input("Ingrese codigo: ")
                 if codigo in Empleados[Id]:
                    print("Dato ya ingresado")
                 else:
                    break
             Empleados[Id][codigo] = {}
             nombrededi = input("Ingrese nombre: ")
     if op == 2:
        print("\nLISTADO")
        listid = list(Empleados.keys())
        ids_ordenado = quick_sort(listid)

        for Id in ids_ordenado:
            datos = Empleados[Id]
            print(f"Codigo: {Id}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Edad: {datos['Edad']}")
            print(f"Sexo: {datos['Sexo']}")
            print(f"Ocupación")
            print(f"Codigo: {codigo}")
            print(f"Nombre: {nombrededi}")
     if op == 3:
        print("Hasta que nos volvamos a ver")
        break
menu()