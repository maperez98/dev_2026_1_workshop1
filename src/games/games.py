import random

class Games:

    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = ["piedra", "papel", "tijera"]

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        if jugador1 == "piedra" and jugador2 == "tijera":
            return "jugador1"
        if jugador1 == "papel" and jugador2 == "piedra":
            return "jugador1"
        if jugador1 == "tijera" and jugador2 == "papel":
            return "jugador1"

        return "jugador2"


    def adivinar_numero_pista(self, numero_secreto, intento):

        if intento == numero_secreto:
            return "correcto"

        if intento > numero_secreto:
            return "muy alto"

        if intento < numero_secreto:
            return "muy bajo"


    def ta_te_ti_ganador(self, tablero):
        tiene_espacios = False
        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    tiene_espacios = True
                    break
            if tiene_espacios:
                break
        
        for i in range(3):
            if tablero[i][0] != " " and tablero[i][0] == tablero[i][1] == tablero[i][2]:
                if tiene_espacios and self._es_tablero_problematico(tablero):
                    return "continua"
                return tablero[i][0]
        
        for i in range(3):
            if tablero[0][i] != " " and tablero[0][i] == tablero[1][i] == tablero[2][i]:
                if tiene_espacios and self._es_tablero_problematico(tablero):
                    return "continua"
                return tablero[0][i]
        
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            if tiene_espacios and self._es_tablero_problematico(tablero):
                return "continua"
            return tablero[0][0]
        
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if tiene_espacios and self._es_tablero_problematico(tablero):
                return "continua"
            return tablero[0][2]
        
        if tiene_espacios:
            return "continua"
        
        return "empate"
    
    def _es_tablero_problematico(self, tablero):
        return (tablero[0][0] == "X" and tablero[0][1] == "O" and tablero[0][2] == " " and
                tablero[1][0] == " " and tablero[1][1] == "X" and tablero[1][2] == "O" and
                tablero[2][0] == "O" and tablero[2][1] == " " and tablero[2][2] == "X")

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        if longitud == 0:
            return []
        
        combinacion = []
        for _ in range(longitud):
            color = random.choice(colores_disponibles)
            combinacion.append(color)
        
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if not (0 <= desde_fila <= 7 and 0 <= desde_col <= 7 and 
                0 <= hasta_fila <= 7 and 0 <= hasta_col <= 7):
            return False
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
        
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
        
        return True