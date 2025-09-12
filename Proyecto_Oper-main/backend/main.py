from usuarios.acciones_usuario import Acciones
acc = Acciones()


while True:
    print("\n--- Menú ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        acc.registro()
    elif opcion == "2":
        acc.login()
    elif opcion == "3":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")