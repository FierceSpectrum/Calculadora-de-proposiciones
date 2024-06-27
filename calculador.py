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
            if valor.upper() == 'V':
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
    local_dict = {'And': And, 'Or': Or, 'Not': Not, 'F': False, 'V': True,
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
    # print(exprecion)

    return proposicion, variables, local_dict, exprecion


# Función para evaluar una expresión lógica
def evaluar_proposicion(expr, valores):
    return expr.subs(valores)


def evaluar_proposicion_con_pasos(expreciones, valores, proposiciones, local_dict):
    pasos = [proposiciones[-1]]
    proposiciones_resultados = []
    letras = list(valores.keys())

    proposicion = proposiciones[-1]
    for letra in letras:
        valor = 'V' if str(valores[letra]) == 'True' else 'F'
        proposicion = proposicion.replace(str(letra), valor)

    pasos.append(proposicion)

    paso_negativos = pasos[-1]
    for i, proposicion in enumerate(proposiciones):
        if '(' in proposicion:
            break
        else:
            for letra in letras:
                if str(letra) in proposicion:
                    valor = 'V' if str(valores[letra]) == 'True' else 'F'
                    proposicion2 = proposicion.replace(str(letra), str(valor))
                    proposicion3 = formato.proposicion_calculable(proposicion)
                    exprecion = trasformar_exprecion(proposicion3, local_dict)
                    resultado = evaluar_proposicion(exprecion, valores)
                    resultado = 'V' if str(resultado) == 'True' else 'F'
                    paso_negativos = paso_negativos.replace(
                        proposicion2, resultado)
                    break

    if paso_negativos != pasos[-1]:
        pasos.append(paso_negativos)

    for i, proposicion in enumerate(proposiciones):
        paso = pasos[-1]
        proposicion2 = proposicion

        if i > 0:
            lista_invert = []
            for j, miniproposicion in enumerate(proposiciones):
                if j >= i:
                    break
                lista_invert.append(miniproposicion)
            lista_invert.reverse()
            resultados_invert = proposiciones_resultados.copy()
            resultados_invert.reverse()

            for j, prop in enumerate(lista_invert):
                if prop in proposicion2:
                    proposicion2 = proposicion2.replace(
                        prop, resultados_invert[j])

        for letra in letras:
            if str(letra) in proposicion2:
                valor = 'V' if str(valores[letra]) == 'True' else 'F'
                proposicion2 = proposicion2.replace(str(letra), str(valor))

        proposicion3 = formato.proposicion_calculable(proposicion)
        proposicion3 = formato.procesar_proposicion(proposicion3)
        exprecion = trasformar_exprecion(proposicion3, local_dict)
        resultado = evaluar_proposicion(exprecion, valores)
        resultado = 'V' if str(resultado) == 'True' else 'F'

        proposiciones_resultados.append(resultado)

        paso = paso.replace(proposicion2, resultado)

        if paso != pasos[-1]:
            pasos.append(paso)

    return pasos

# Función para simplificar una expresión lógica
def simplificar_proposicion(expr):
    return simplify(expr)



def calcular_exprecion():
    proposicion, variables, local_dict, exprecion = calcular()

    exprecion = trasformar_exprecion(exprecion, local_dict)

    # Pedimos los valores de las variables
    valores = pedir_valores(variables)

    # Obtenemos las expreciones y proposiciones
    expreciones, proposiciones = texto_exprecion(proposicion)

    # Convertir las cadenas de texto a una expresión de SymPy
    expreciones_simpy = trasformar_expreciones(expreciones, local_dict)

    pasos = evaluar_proposicion_con_pasos(
        expreciones_simpy, valores, proposiciones, local_dict)

    pasos = formato.texto_centrado(pasos)

    for paso in pasos:
        print(paso)

    return pasos


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
    encabezado = [str(var) for var in variables] + [str(exprecion)
                                                    for exprecion in expreciones_simpy]
    tabla_verdad.append(encabezado)

    # Evaluar la expresión para cada combinación de valores de verdad
    for combinacion in combinaciones:

        # Crear un diccionario con las valores y combinaciones: { P:True, Q:False, ... }
        valores = dict(zip(variables, combinacion))

        # Obtiene el resultado de la expresion en base a los valores
        resultados = [exprecion_simpy.subs(valores)
                      for exprecion_simpy in expreciones_simpy]

        # Crea una lista de las combinaciones mas el resultado: [ True, False ] + [ True ]
        fila = list(combinacion) + resultados

        # Agrega la fila en la tabla.
        tabla_verdad.append(fila)

    # Imprimir la tabla de verdad
    for fila in tabla_verdad:
        print("\t".join(map(str, fila)))


calcular_exprecion()
