from unittest import TestCase

from ProcesadorNumeros import ProcesadorNumeros


class ProcesadorNumerosTest(TestCase):
    def test_procesar(self):
        result = {0, 0, 0, 0}
        self.assertItemsEqual(self,  result, ProcesadorNumeros().procesar(""), "Cadena vacia");
