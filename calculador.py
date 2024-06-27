import sympy
from sympy import symbols, And, Or, Not, Implies, Equivalent, simplify
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, BooleanTrue, BooleanFalse
from itertools import product

import formato


def pedir_proposicion():
    proposicion = input('ingrese la proposicion: ')
    # proposicion = "((P ∧ Q) ⇄ ((¬R ∧ (Q ∨ ¬P)) ⇾ ¬(P ∨ (R ∧ ¬Q))))"
    return proposicion


def pedir_valores(variables):
    valores = {}
    for variable in variables:
        while True:
            valor = input(f'Ingrese el valor de {variable}: ')
            if valor.upper() == 'T':
                valor = True
                break
            elif valor.upper() == 'F':
                valor = False
                break
            else:
                print('Solo se permieten valores de True o False')

        valores[variable] = valor
    return valores


def texto_exprecion(proposicion):
    lista_proposiciones = formato.separar_proposicion(proposicion)
    lista_expreciones = []
    for miniproposicion in lista_proposiciones:
        exprecion = formato.procesar_proposicion(miniproposicion)
        lista_expreciones.append(exprecion)
    lista_expreciones.append(exprecion)
    return lista_expreciones, lista_proposiciones


def trasformar_exprecion(exprecion, local_dict):
    return sympy.sympify(exprecion, locals=local_dict)


def trasformar_expreciones(expreciones, local_dict):
    expreciones_simpy = []
    for exprecion in expreciones:
        expresion_simpy = trasformar_exprecion(exprecion, local_dict)
        expreciones_simpy.append(expresion_simpy)

    return expreciones_simpy


def calcular_local_disct(variables):
    local_dict = {'And': And, 'Or': Or, 'Not': Not,
                  'Implies': Implies, 'Equivalent': Equivalent}
    for variable in variables:
        local_dict[str(variable)] = variable
    return local_dict


def calcular():
    # Pedimos la proposicion
    proposicion = pedir_proposicion()

    # Obtenemos las letras de la proposicion en formato texto
    letras_unicas = formato.extraer_variables(proposicion)

    # Unimos las letras
    letras = formato.pegar_letras(letras_unicas)

    # Cremos las variables
    variables = symbols(letras)

    # Creamos un diccionario que mapea los nombres de las funciones a las funciones reales
    local_dict = calcular_local_disct(variables)

    exprecion = formato.procesar_proposicion(proposicion)
    print(exprecion)

    return proposicion, variables, local_dict, exprecion


# Función para evaluar una expresión lógica
def evaluar_proposicion(expr, valores):
    return expr.subs(valores)

# Función para simplificar una expresión lógica
def simplificar_proposicion(expr):
    return simplify(expr)


def calcular_exprecion():
    proposicion, variables, local_dict, exprecion = calcular()

    exprecion = trasformar_exprecion(exprecion, local_dict)

    # Pedimos los valores de las variables
    valores = pedir_valores(variables)

    resultado = evaluar_proposicion(exprecion, valores)

    print(resultado)

    return(resultado)

def calcular_simplificacion():
    proposicion, variables, local_dict, exprecion = calcular()

    exprecion = trasformar_exprecion(exprecion, local_dict)

    resultado = simplificar_proposicion(exprecion)

    print(resultado)

    return resultado

def calcular_tabla():
    proposicion, variables, local_dict, exprecion = calcular()

    # Obtenemos las expreciones y proposiciones
    expreciones, proposiciones = texto_exprecion(proposicion)

    # Convertir las cadenas de texto a una expresión de SymPy
    expreciones_simpy = trasformar_expreciones(expreciones, local_dict)
    exprecion_simpy = trasformar_exprecion(exprecion, local_dict)

    # Generar todas las combinaciones posibles de valores de verdad
    combinaciones = list(product([True, False], repeat=len(variables)))

    # Generar la tabla de verdad
    tabla_verdad = []

    # Encabezado de la tabla
    encabezado = [str(var) for var in variables] + [str(exprecion) for exprecion in expreciones_simpy]
    tabla_verdad.append(encabezado)

    # Evaluar la expresión para cada combinación de valores de verdad
    for combinacion in combinaciones:

        # Crear un diccionario con las valores y combinaciones: { P:True, Q:False, ... }
        valores = dict(zip(variables, combinacion))

        # Obtiene los resultados de la expresiones en base a los valores
        resultados = [exprecion_simpy.subs(valores) for exprecion_simpy in expreciones_simpy]

        # Crea una lista de las combinaciones mas los resultados: [ True, False ] + [ True ]
        fila = list(combinacion) + resultados

        # Agrega la fila en la tabla.
        tabla_verdad.append(fila)
    
    # Imprimir la tabla de verdad
    for fila in tabla_verdad:
        print("\t".join(map(str, fila)))





