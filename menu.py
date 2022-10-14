# Menu, es donde se efecutan las funciones y hace juncionar al juego
# Carla S. Centeleghe

from juego import Jugador
from colorama import init, Fore, Style
from tablero import Tablero

# Clase principal, que hace funcionar el programa
class Menu:
    def __init__(self) -> None:
        pass
    # Funcion que comienza a correr el juego
    def main():
        while True:
            # Imprimo por pantalla (con colorcito) el nombre del juego
            print(Fore.YELLOW + "4" + " " + Fore.GREEN + "E" + Fore.BLUE + "N" + " " + Fore.RED +
                "L" + Fore.CYAN + "i" + Fore.MAGENTA + "N" + Fore.WHITE + "E" + Fore.YELLOW + "A\n") 

            # Imprimo por pantalla un indice de opciones
            arbol_b = input("1- UNO vs UNO"
                            "\n"
                            "2- Salir"
                            "\n"
                            "Elige: ")
            if arbol_b == "2":
                break
            if arbol_b == "1":
                # Empieza a ejecutar y llamar junciones
                while True: 
                    tablero = Tablero.crear_tablero() # Creo el tablero

                    Tablero.unoVSuno(tablero) # Juego el juego

                    Tablero.pinta_otra() #Revancha, vuelve a ejecutarel prograa/ NO FUNCIONA

                 
if __name__ == "__main__":

    t1 = Tablero()
    t1.crear_tablero()

    j1 = Jugador()
    j1.color_jugador()

    j2 = Jugador()
    j2.color_jugador()
    t1.unoVSuno(j1, j2)

    t1.pinta_otra()


                    


