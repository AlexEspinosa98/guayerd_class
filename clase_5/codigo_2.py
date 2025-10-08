

# Quiero una funcion que cuando reciba un numero 
# lo multiplique por 2, lo imprima y luego retorne el resultado

while True:
    print("\nMenú de opciones:")
    print("1. Información 1")
    print("2. Información 2")
    print("3. Información 3")
    print("4. Información 4")
    print("0. Salir")
    opcion = input("Elige una opción (0-4): ")
    if opcion == "0":
        print("Saliendo del programa.")
        break
    elif opcion == "1":
        print("Has elegido la opción 1: Información 1")
    elif opcion == "2":
        print("Has elegido la opción 2: Información 2")
    elif opcion == "3":
        print("Has elegido la opción 3: Información 3")
    elif opcion == "4":
        print("Has elegido la opción 4: Información 4")
    else:
        print("Opción inválida. Por favor, elige una opción entre 0 y 4.")