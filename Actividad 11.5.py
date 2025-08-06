Empleados = {}
def menu():
    while True:
        print("Menu")
        print("1.Ingreso")
        print("2.Presentar")
        print("3.Buscar")
        print("4.Eliminar")
        op = int(input("Ingrese un opcion: "))
        if op == 1:
            cantidad = int(input("Ingrese la cantidad de elementos: "))
            for i in range(cantidad):
                print(f"elementos {i+1}")
                while True:
                    Id = int(input("Ingrese ID del elemento: "))
                    if Id in Empleados:
                     print("Ya esta ingresado")
                    else:
                        Empleados[Id] = {}
                        break
                Empleados[Id]["Nombre"] = input("Ingrese el nombre: ")
                Empleados[Id]["edad"] = int(input("Ingrese la edad: "))
                Empleados[Id]["dedicación"] = {}
                cantidedi = input("Ingrese la cantidad de elementos: ")
                for i in range(cantidad):
                    print(f"elementos {i+1}")
                    while True:
                          codidedi = input("Ingrese el codigo: ")
                          if codidedi in Empleados[Id]:
                            print("ya ingresado")
                          else:
                            Empleados[Id][codidedi] = {}
                            break
                    nombrededi = input("Ingrese el nombre de la dedicación: ")

        if op == 2:
            print("\nLISTADO")
            for Id, datos in Empleados.items():
                print(f"codigo {Id}")
                print(f"nombre: {datos['Nombre']}")
                print(f"edad: {datos['edad']}")
                print(f"codigo del viaje {codidedi}")
                print(f"nombre de la dedicación {nombrededi}")
        if op == 3:
            print("Hasta que nos volvamos a ver")
            break
menu()