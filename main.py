#Programa de ChatGPT

estacionamiento = 5
autos = 0

while True:
    print("\n--- ESTACIONAMIENTO ---")
    print("1. Entrar auto")
    print("2. Salir auto")
    print("3. Ver espacios disponibles")
    print("4. Salir del programa")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if autos < estacionamiento:
            autos = autos + 1
            print("Auto registrado.")
        else:
            print("Estacionamiento lleno.")

    elif opcion == "2":
        if autos > 0:
            autos = autos - 1
            print("Auto retirado.")
        else:
            print("El estacionamiento está vacío.")

    elif opcion == "3":
        print("Espacios disponibles:", estacionamiento - autos)

    elif opcion == "4":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")

