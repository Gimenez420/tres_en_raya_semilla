def comprobar_ganador(x, y, tablero):

    # ¿Qué casilla tenemos que comprobar?
    jugador = tablero[x][y]
    print("Voy a comprobar ", jugador, " en ", x, ",", y)

    if jugador == '-':
        return False
    
    tamanyo = len(tablero)

    ##########################################
    # Miramos hacia la izquierda y derecha

    victoria_fila = True

    # TODO: comprobacion
    pass
    
    if victoria_fila:
        return True
    ##########################################
    # Miramos hacia abajo
    victoria_columna = True

    # TODO: comprobacion
    pass

    if victoria_columna:
        return True
    ##########################################
    # Diagonal
    victoria_diagonal = True
        

    return False


def mostrar_tablero(tablero):
    for linea in tablero:
        print(linea)

# X --> 1
# O --> -1
# - --> 0
def convertir_tablero(tablero):
    nuevo_tablero = []
    for linea in tablero:
        lista = []
        for char in linea:
            if char == 'X':
                lista.append(1)
            elif char == 'O':
                lista.append(-1)
            else:
                lista.append(0)
        nuevo_tablero.append(lista)
    ##########################################
    #TODO: Convertirlo a una lista de listas
    # ej: [[1,1,0], [1,-1,-1], [0, 0, 0]]

    return nuevo_tablero
