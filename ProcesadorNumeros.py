class ProcesadorNumeros:
    def procesar(self, cadena):
        if (cadena==""):
            cantidad=0
        elif ("," in cadena):
            cantidad=len(cadena.split(","))
        else:
            cantidad = 1
        if (cadena==""):
            minimo = 0
        elif(len(cadena)==1):
            minimo= int(cadena)
        else:
            minimo= 0
        return {cantidad, minimo, 0, 0}

