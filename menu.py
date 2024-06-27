import calculador


def evaluar_Proposicion():
    calculador.calcular_exprecion()


def simplificar_Proposicion():
    calculador.calcular_simplificacion()


def tabla_de_Verdad():
    calculador.calcular_tabla()


def menu():
    while True:
        menu = """
        --- Calculadora de Proposiciones ---

            1. Evaluar Proposicion
            2. Simplificar Proposicion
            3. Tabla de Verdad
            4. Salir del Menu

        ---                              ---
            Ingrese una opcion: """

        opcion = input(menu)
        if opcion in ("1", "2", "3", "4"):
            if opcion == "1":
                evaluar_Proposicion()
            elif opcion == "2":
                simplificar_Proposicion()
            elif opcion == "3":
                tabla_de_Verdad()
            elif opcion == "4":
                break
        else:
            print("            IIngrese una opcion valida! ")


menu()
