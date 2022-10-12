# Menu donde se van a colocar los input
# Carla S. Centeleghe

from colorama import init, Fore, Style

class Menu:
    def __init__(self) -> None:
        pass

    #hace funcionear el codigo
    def main():
        while True:
            print(Fore.YELLOW + "4" + " " + Fore.GREEN + "E" + Fore.BLUE + "N" + " " + Fore.RED +
                "L" + Fore.CYAN + "i" + Fore.MAGENTA + "N" + Fore.WHITE + "E" + Fore.YELLOW + "A\n")

            print
            arbol_b = input("1- UNO vs UNO"
                            "\n"
                            "2- Salir"
                            "\n"
                            "Elige: ")
            if arbol_b == "2":
                break
            if arbol_b == "1":
                pass
