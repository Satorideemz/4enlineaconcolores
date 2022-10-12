# Juego del juego
# Carla S. Centeleghe

from tablero import *

class Jugador:
    def __init__(self, nrojugador, ficha, color):
        self.nrojugador = nrojugador
        self.ficha = ficha
        self.color = color
        self.VIOLETA="X"
        self.AZUL="O"


    # Defino los colores de los jugadores
    def color_jugador(self):

        if self.nrojugador==1:
            self.color="VIOLETA"
        if self.nrojugador==2:
            self.color = "AZUL"

        return self.color

    # Contar las fichas, para ver la comdicion de ganar
    def definir_ganador_cotar_fichas(self, ficha,tablero):
        # Cuento las fichas horizontalmente
        for posicion in range(5):
            for i in range(8):
                if tablero[i][posicion] == ficha and tablero[i][posicion+1] == ficha and tablero[i][posicion+2] == ficha and tablero[i][posicion+3] == ficha and tablero[i][posicion+4]:
                    return True

        # Cuento las fihcas verticalmente
        for possicion in range(8):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i+1][possicion] == ficha and tablero[i+2][possicion] == ficha and tablero[i+3][possicion] == ficha and tablero[i+4][possicion]:
                    return True



