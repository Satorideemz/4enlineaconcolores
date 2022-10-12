# Tablero del juego 
# Carla S. Centeleghe

from colorama import init, Fore, Style
from juego import *

init(autoreset=True)

# Declavo algunas variables utiles
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2

class Tablero:

    def __init__(self):
        self.fila = 8
        self.columna = 8
        self.tablero = []

    def crear_tablero(self):
        tablero = []
        for fila in range(self.fila):
            self.tablero.append([])
            for self.columna in range(8):
                self.tablero[fila].append(" ")
        return self.tablero

    # Input para la ficha
    def pido_ficha(possicion):
        possicion = int(input("Ingresa la columna para colocar la pieza: "))
        return possicion

    # Este metodo tirar las fichas y revisa que no este llena la columna
    def ingresar_ficha(self,ficha):
        possicion = self.pido_ficha()
        for i in reversed(range(self.columna)):
            if self.tablero[1][possicion] == ficha:
                print("columna llena!!! sos un pelotudo")
                break
            if self.tablero[i+1][possicion] == " ":
                self.tablero[i+1][possicion] = ficha
                break
      
    # Como se imprime por pantalla
    def imprimir_tablero(tablero):
        print("|", end="")
        for f in range(1, len(tablero)):

            print(f, end="|")
        print("")
        # Colores
        for fila in tablero:
            print("|", end="")
            for valor in fila:
                color_terminal = Fore.MAGENTA
                if valor == AZUL:
                    color_terminal = Fore.CYAN
                print(color_terminal + valor, end="")
                print(end="")
                print("|", end="")
            print("")
        # Final
        print("+", end="")
        for f in range(1, len(tablero)):
            print("-", end="+")
        print("")

    # Imprimo un ganaste al gandor
    def ganador_felicitaciones(jugador_actual):
        if jugador_actual == JUGADOR_1:
            print(Fore.MAGENTA + "Jugador 1\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")
        else:
            print(Fore.CYAN + "Jugador 2\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")

    # Turnos y colores
    def turnos_colores(turno):
        print(Fore.MAGENTA +
              "Jugador 1: {VIOLETA} " + Fore.CYAN + "| Jugador 2: {AZUL}")
        if turno == JUGADOR_1:
            print("Juega el " + Fore.MAGENTA + "jugador 1 ({VIOLETA})")
        else:
            print("Juega el " + Fore.CYAN + "jugador 2 ({AZUL})")
        
    #otra partida boucle
    def pinta_otra():
        while True:
            eleccion = input("¿Revancha? [S/N] ")()
            if eleccion == "S":
                return True
            elif eleccion == "N":
                return False


#main temporal
# t1=Tablero()
# t1.crear_tablero()
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")
# t1.ingresar_ficha(3, "x")

#t1.coulmna_valida(9)
#print(t1.tablero)

