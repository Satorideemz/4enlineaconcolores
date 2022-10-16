# Test para todo el codigo

#from distutils.command.build import build
#from msilib.schema import Patch
import unittest
import unittest.mock
from juego import Jugador

from tablero import Tablero
#from juego import Jugador
#from menu import Menu


class Test4enLinea(unittest.TestCase):
    # Test para el funcionamiento la creacion del tablero
    def test_setUp_1(self):
        tablero = Tablero()
        tablero.crear_tablero()
        self.assertEqual(len(tablero.tablero), 8)

    def test_setUp_2(self):
        tablero = Tablero()
        tablero.crear_tablero()
        for x in range(8):
            self.assertEqual(len(tablero.tablero[x]), 8)

     #Test para ver si puedo ingresar los input
    @unittest.mock.patch('tablero.Tablero.pido_ficha', return_value=3)
    def test_pido_ficha_3(self, name):
        possicion = Tablero.pido_ficha()
        self.assertEqual(possicion, 3)

    # Test para felicitacion ganador, verificamos que la funcion printe
    def test_print_4(self):
        print("Test: test_print_4")

    #Test para ver si puedo jugar otra
    @unittest.mock.patch('tablero.Tablero.pinta_otra', return_value="S")
    def test_pinta_otra_5(self, name):
        eleccion = Tablero.pinta_otra()
        self.assertTrue(eleccion)

    @unittest.mock.patch('tablero.Tablero.pinta_otra', return_value="N")
    def test_pinta_otra_6(self, name):
        eleccion = Tablero.pinta_otra()
        self.assertTrue(eleccion)

    # Test para ver las fichas de los jugadores
    def test_color_jugador_7(self):
        Jugador.nrojugador = 1
        resultado = Jugador.color_jugador(Jugador)
        self.assertEqual(resultado, "x")

    def test_color_jugador_8(self):
        Jugador.nrojugador = 2
        resultado = Jugador.color_jugador(Jugador)
        self.assertEqual(resultado, "o")



    # Test para ver si ingresa la ficha en el tablero / NO FUNCIONA
    # @unittest.mock.patch('tablero.Tablero.ingresar_ficha', side_effect=[3,'x'])
    # def test_ingreso_ficha_4(self, name):
    #     juego = Tablero()
    #     juego.crear_tablero()
    #     self.assertTrue(Jugador.definir_ganador_cotar_fichas(self, 'x', juego.tablero))


    # Test de como imprime en pantalla / NO FUNCIONA
    # def test_iprimir_tablero(self):
    #     tablero = Tablero
    #     self.assertTrue(tablero.imprimir_tablero(self))


    def test_ganador_horizontal_x(self):
        juego =  Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(1, 'x')
        juego.ingresar_ficha(2, 'x')
        juego.ingresar_ficha(3, 'x')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(self, 'x', juego.tablero))

    def test_ganador_vertical_x(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(self, 'x', juego.tablero))
    

if __name__ == "__main__":
    unittest.main()
