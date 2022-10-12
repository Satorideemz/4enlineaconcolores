# Test para todo el codigo

#from distutils.command.build import build
#from msilib.schema import Patch
import unittest

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

    # Test para ver si puedo ingresar los input FUNCIONA
    #def test_pido_ficha_3(self):
    #    possicion = Tablero.pido_ficha(3)
    #    self.assertEqual(possicion, 3)

    # Test para ver si ingresa la ficha
    # def test_ingresar_ficha(self):
    #     tablero = Tablero()
    #     entradas=[1]
    #    for i in range (len(entradas)):
    #     tablero.ingresar_ficha(3,"X")

    #     self.assertDictEqual(tablero.__dict__, {
    #     })



if __name__ == "__main__":
    unittest.main()
