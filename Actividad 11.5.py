Empleados = {}
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
                 Empleados[Id] = {}
                 break
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
                    Empleados[Id][codigo] = {}
                    break
             nombrededi = input("Ingrese nombre: ")
     if op == 2:
        print("\nLISTADO")
        for Id, datos in Empleados.items():
            print(f"Codigo: {Id}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Edad: {datos['Edad']}")
            print(f"Sexo: {datos['Sexo']}")
            print(f"Ocupación")
            print(f"codigo de la ocupación: {codigo}")
            print(f"Nombre de la ocupación: {nombrededi}")
     if op == 3:
        print("Hasta que nos volvamos a ver")
        break
menu()