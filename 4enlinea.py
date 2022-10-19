
class Tablero:
    
    def __init__(self):
        self.fila=8
        self.columna=8
        self.tablero=[]

    def crear_tablero(self):
        tablero = []
        for fila in range(self.fila):
            self.tablero.append([])
            for self.columna in range(8):
                self.tablero[fila].append(" ")
        return self.tablero


    def lugar_vacio(self,ficha):
        #revisar este metodo, no se si esta bien
        #rehacer posiblemente
        indice = len(self.tablero) - 1
        while indice >= 0:
            if self.tablero[indice][ficha] == " ":
                return indice
            indice -= 1
        return -1

    def ingresar_ficha(self,posicion,ficha):
        #este metodo por alguna razon empieza a tirar la ficha desde una posicion mas arriba
        for i in reversed(range(self.columna)):
            if self.tablero[i][posicion]==" ":
                self.tablero[i][posicion]=ficha
                break        
                

    def coulmna_valida(self,columna):

        while True:
            if columna <= 0 or columna > 8:
                print("Columna no válida")
            #contemplar caso de columna llena
            #    print("Esa columna ya está llena")
            else:
                return True


class Jugador:
    def __init__(self,nrojugador,ficha,color):
        self.nrojugador=nrojugador
        self.ficha=ficha
        self.color=color

#    def asignar_color():
#        color = VIOLETA
#        if jugador == JUGADOR_2:
#            color = AZUL
#        return color    



class Display:
    def __init__(self) -> None:
        pass

class Menu:
    def __init__(self) -> None:
        pass





#main temporal

#t1=Tablero()
#t1.crear_tablero()
#t1.ingresar_ficha(3,"x")
#t1.ingresar_ficha(3,"x")

#print(t1.tablero)
#print(t1.lugar_vacio(2))
