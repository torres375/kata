from unittest import TestCase

from ProcesadorNumeros import ProcesadorNumeros


class ProcesadorNumerosTest(TestCase):
    def test_procesar(self):
        result = {0, 0, 0, 0}
        self.assertEqual(ProcesadorNumeros().procesar(""), result, "Cadena vacia");