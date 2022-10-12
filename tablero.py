# Tablero del juego 
# Carla S. Centeleghe

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


    def ingresar_ficha(self, posicion, ficha):
        #este metodo tirar las fichas y revisa que no este llena la columna

        for i in reversed(range(self.columna)):
            if self.tablero[1][posicion] == ficha:
                print("columna llena!!! sos un pelotudo")
                break
            if self.tablero[i+1][posicion] == " ":
                self.tablero[i+1][posicion] = ficha
                break



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

