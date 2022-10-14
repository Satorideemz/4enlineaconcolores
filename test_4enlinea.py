# Test para todo el codigo

#from distutils.command.build import build
#from msilib.schema import Patch
import unittest
import unittest.mock

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

    # Test para ver si ingresa la ficha en el tablero / NO FUNCIONA
    # @unittest.mock.patch('tablero.Tablero.ingresar_ficha', side_effect=[3,'x'])
    # def test_ingreso_ficha_4(self, name):
    #    x = Tablero()
    #    self.assertEqual(x.ingresar_ficha[1], 'x')

    # Test de como imprime en pantalla / NO FUNCIONA
    # def test_iprimir_tablero(self):
    #     tablero = Tablero
    #     self.assertTrue(tablero.imprimir_tablero(self))

    # Test para felicitacion ganador
   


    

if __name__ == "__main__":
    unittest.main()
