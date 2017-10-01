class ProcesadorNumeros:
    def procesar(self, cadena):
        if (cadena==""):
            cantidad=0
        elif ("," in cadena):
            cantidad=len(cadena.split(","))
        else: 
            cantidad=1
        minimo = 0
        return {cantidad, minimo, 0, 0}
