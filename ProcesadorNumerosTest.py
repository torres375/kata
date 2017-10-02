from unittest import TestCase

from ProcesadorNumeros import ProcesadorNumeros


class ProcesadorNumerosTest(TestCase):
    def test_procesarCantidad(self):
        result = {0, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar(""), result, "Cadena vacia");

    def test_procesar1NumeroCantidad(self):
        result = {1, 4, 4, 4}
        self.assertEqual(ProcesadorNumeros().procesar("4"), result, "Cadena Con Un Numero");

        def test_procesarCadenaDosNumerosCantidad(self):
        result = {2, 3, 9, 6}
        self.assertEqual(ProcesadorNumeros().procesar("9,3"), result, "Cadena Con dos Numeros");

    def test_procesarCadenaconNNumerosCantidad(self):
        result = {11, -1, 9, 0}
        self.assertEqual(ProcesadorNumeros().procesar("2,4,-1,0,5,1,3,6,7,8,9"), result, "Cadena Con N Numeros");
