class ProcesadorNumeros:
    def procesar(self, cadena):
        if (cadena==""):
            cantidad=0
        elif ("," in cadena):
            cantidad=2
        else: 
            cantidad=1
        return {cantidad, 0, 0, 0}
