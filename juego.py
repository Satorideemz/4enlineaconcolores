# Juego del juego
# Carla S. Centeleghe

import random
from tablero import Tablero

# Declavo algunas variables utiles
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2


class Jugador:
    def __init__(self, ficha):
         self.ficha = ficha

    # Defino los colores de los jugadores
    def color_jugador(turno):
        ficha = VIOLETA
        if turno == JUGADOR_2:
            ficha = AZUL
        return ficha

    # Contar las fichas, para ver la comdicion de ganar
    def definir_ganador_cotar_fichas(self, ficha,tablero):

        # Cuento las fihcas verticalmente
        for possicion in range(8):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i+1][possicion] == ficha and tablero[i+2][possicion] == ficha and tablero[i+3][possicion] == ficha and tablero[i+4][possicion]:
                    return True

        # Cuento las fichas horizontalmente
        for posicion in range(5):
            for i in range(8):
                if tablero[i][posicion] == ficha and tablero[i][posicion+1] == ficha and tablero[i][posicion+2] == ficha and tablero[i][posicion+3] == ficha and tablero[i][posicion+4]:
                    return True

        # Cuento las fichas diagonalmente positivo
        for possicion in range(5):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i+1][possicion+1] == ficha and tablero[i+2][possicion+2] == ficha and tablero[i+3][possicion+3] == ficha and tablero[i+4][possicion+4]:
                    return True

        # Cuento las diagonales negativo
        for possicion in range(5):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i-1][possicion+1] == ficha and tablero[i-2][possicion+2] == ficha and tablero[i-3][possicion+3] == ficha and tablero[i-4][possicion+4]:
                    return False
        return False

    # Elige el jugador que va a empezar el juego, es al azar. Porq uso una libreria para ello
    def elegir_jugador():
        return random.choice([JUGADOR_1, JUGADOR_2])
    
    #Juego 1vs1, donde se llaman a la malloria de las funciones
    def unoVSuno(tablero):
       turno = Jugador.elegir_jugador()
       ficha_jugada = Jugador.color_jugador(turno)#aca se le asigna una "x" o un "O" a ficha
       while True:

            Tablero.imprimir_tablero(tablero)
            Tablero.turnos_colores(turno)
            Tablero.pido_ficha()
            Tablero.ingresar_ficha(ficha_jugada)

            ganador = Jugador.definir_ganador_cotar_fichas(ficha_jugada, tablero)

            if ganador:
                Tablero.ganador_felicitaciones(turno)
                break
            else:  # cambia los jugadores, va dando los turnos
                if turno == JUGADOR_1:
                    turno = JUGADOR_2
                else:
                    turno = JUGADOR_1




        

#j1=Jugador(1)
#print(j1.elegir_jugador())
 
