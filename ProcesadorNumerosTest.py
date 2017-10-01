from unittest import TestCase

from ProcesadorNumeros import ProcesadorNumeros


class ProcesadorNumerosTest(TestCase):
    def test_procesarCantidad(self):
        result = {0, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar(""), result, "Cadena vacia");

    def test_procesar1NumeroCantidad(self):
        result = {1, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar("4"), result, "Cadena Con Un Numero");

    def test_procesarCadenaDosNumerosCantidad(self):
        result = {2, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar("2,4"), result, "Cadena Con dos Numeros");

    def test_procesarCadenaconNNumerosCantidad(self):
        result = {5, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar("2,4,5,6,8"), result, "Cadena Con N Numeros");

    def test_procesarMinimo(self):
        result = {0, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar(""), result, "Cadena vacia");
