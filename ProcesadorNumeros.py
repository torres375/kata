class ProcesadorNumeros:
    def procesar(self, cadena):
        if (cadena==""):
            cantidad=0
        elif ("," in cadena):
            cantidad=len(cadena.split(","))
        else:
            cantidad = 1
        maximo = 0
        minimo = 0
        sumatoria = 0
        if(len(cadena)==1):
            minimo= int(cadena)
            maximo= int(cadena)
        elif(len(cadena)>1):
            numeros = cadena.split(",")
            for n in numeros:
                if (minimo > int(n)):
                    minimo = int(n)
                if (maximo < int(n)):
                    maximo = int(n)
        if (cantidad > 0):
            promedio = sumatoria / cantidad
        else:
            promedio = 0
        return {cantidad, minimo, maximo, promedio}
