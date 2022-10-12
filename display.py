# Displey es lo que imprime por terminal (bonito)
# Carla S. Centeleghe

from colorama import init, Fore, Style

init(autoreset=True)

class Display:
    def __init__(self) -> None:
        pass

    # # como se imprime por pantalla
    # def imprimir_tablero(tablero):
    #     print("|", end="")
    #     for f in range(1, len(tablero)):

    #         print(f, end="|")
    #     print("")
    # # Colores
    #     for fila in tablero:
    #         print("|", end="")
    #         for valor in fila:
    #             color_terminal = Fore.MAGENTA
    #             if valor == AZUL:
    #                 color_terminal = Fore.CYAN
    #             print(color_terminal + valor, end="")
    #             print(end="")
    #             print("|", end="")
    #         print("")
    # # Final
    #     print("+", end="")
    #     for f in range(1, len(tablero)):
    #         print("-", end="+")
    #     print("")
