def proposicion_calculable(proposicion):
    proposicion = proposicion.replace(
        '¬', '~').replace('∧', '&').replace('∨', '|')
    return proposicion


def procesar_proposicion(proposicion):
    symbol_Implies = '⇾'
    symbol_Equivalent = '⇄'
    symbol_And = '∧'
    Symnol_Or = '∨'
    Symbol_Not = '¬'

    def agregar(proposicion, simbolo, palaba):
        nivel = 0
        indices_parentesis = []
        for i, char in enumerate(proposicion):
            if char == "(":
                nivel += 1
                indices_parentesis.append(i)
            elif char == ")":
                nivel -= 1
                indices_parentesis.pop()

            if char == simbolo and indices_parentesis:
                inicio = indices_parentesis[-1]
                proposicion = f"{proposicion[:inicio]}{palaba}{
                    proposicion[inicio:i-1]},{proposicion[i + 1:]}"
                break
        return proposicion

    def agregar2(proposicion, simbolo, palaba):
        for i, char in enumerate(proposicion):
            siguiente = proposicion[i+1]
            if char == simbolo and siguiente != '(':
                proposicion = f"{proposicion[:i]}{
                    palaba}({proposicion[i+1:i+2]}){proposicion[i+2:]}"
                break
            elif char == simbolo and proposicion[i+1] == '(':
                nivel = 0
                indices_parentesis = []
                for j, char2 in enumerate(proposicion[i+1:]):
                    if char2 == "(":
                        nivel += 1
                        indices_parentesis.append(j)
                    elif char2 == ")":
                        nivel -= 1

                    if nivel == 0:
                        proposicion = f"{proposicion[:i]}{
                            palaba}({proposicion[i+1:i+1+j]}){proposicion[i+1+j:]}"
                        break
                break
        return proposicion

    while symbol_Equivalent in proposicion or symbol_Implies in proposicion or symbol_And in proposicion or Symnol_Or in proposicion or Symbol_Not in proposicion:
        if Symbol_Not in proposicion:
            proposicion = agregar2(
                proposicion, Symbol_Not, 'Not')

        elif symbol_Implies in proposicion:
            proposicion = agregar(proposicion, symbol_Implies, 'Implies')

        elif symbol_Equivalent in proposicion:
            proposicion = agregar(
                proposicion, symbol_Equivalent, 'Equivalent')

        elif symbol_And in proposicion:
            proposicion = agregar(
                proposicion, symbol_And, 'And')

        elif Symnol_Or in proposicion:
            proposicion = agregar(
                proposicion, Symnol_Or, 'Or')

    return proposicion


def proposicion_mostrable(proposicion):

    def quitar_funcion(proposicion, simbolo):
        proposicion2 = ""
        nivel = 0
        for i, char in enumerate(proposicion):
            if char == "(":
                nivel += 1
            elif char == ")":
                nivel -= 1

            if nivel == 1 and char == ",":
                proposicion2 = f"{proposicion[:i]} {simbolo}{
                    proposicion[i+1:]}"
                break

        return (proposicion2)

    while 'Implies' in proposicion or 'Equivalent' in proposicion:
        for i, char in enumerate(proposicion):
            if char == "I":
                proposicion2 = quitar_funcion(
                    proposicion[i + 7:], "⇾")
                proposicion = proposicion[:i] + proposicion2
                break
            elif char == "E":
                proposicion2 = quitar_funcion(
                    proposicion[i + 10:], "⇄")
                proposicion = proposicion[:i] + proposicion2
                break
    proposicion3 = proposicion.replace(
        '~', '¬').replace('&', '∧').replace('|', '∨')
    return proposicion3


def separar_proposicion(proposicion):
    # proposicion2 = proposicion.replace(' ', '')
    proposicion2 = proposicion
    lista = []
    nivel = 0
    listaInicio = []
    for i, char in enumerate(proposicion2):
        if i < len(proposicion2)-1:
            siguiente = proposicion2[i+1]
        if char == '¬' and siguiente != '(':
            lista.append(proposicion[i:i+2])

    for i, char in enumerate(proposicion2):
        
        if char == '(':
            nivel += 1
            listaInicio.append(i+1)
        elif char == ')':
            nivel -= 1
            inicio = listaInicio.pop()
            lista.append(proposicion2[inicio-1:i+1])
            anterios = proposicion2[inicio-2]
            if anterios == '¬':
                lista.append(proposicion2[inicio-2:i+1])

    return lista


def extraer_variables(proposicion):
    lista_caracteres = ['¬', '∧', '∨', '⇄', '⇾', '(', ')', ' ']
    remplaso = ''
    for caracter in lista_caracteres:
        proposicion = proposicion.replace(caracter, remplaso)

    caracteres_unicas = []

    for char in proposicion:
        if not (char in caracteres_unicas):
            caracteres_unicas.append(char)

    return caracteres_unicas


def pegar_letras(letras):
    letras = ' '.join(letras)
    return letras


# proposicion = "(((P ∧ Q) ⇄ ((¬R ∧ (Q ∨ ¬P)) ⇾ ¬(P ∨ (R ∧ ¬Q)))))"
# resultado = extraer_variables(proposicion)
# print(resultado)
