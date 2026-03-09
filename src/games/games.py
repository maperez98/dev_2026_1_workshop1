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

        # revisar filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] and fila[1] == fila[2]:
                return fila[0]

        # revisar columnas
        for i in range(3):
            if tablero[0][i] != " " and tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
                return tablero[0][i]

        # diagonal principal
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
            return tablero[0][0]

        # diagonal secundaria
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        # revisar si quedan espacios
        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass