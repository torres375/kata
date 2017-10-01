class ProcesadorNumeros:
    def procesar(self, cadena):
        if (cadena==""):
            cantidad=0
        elif ("," in cadena):
            cantidad=len(cadena.split(","))
        else:
            cantidad = 1

        minimo = 0
        if(len(cadena)==1):
            minimo= int(cadena)
        elif(len(cadena)>1):
            numeros = cadena.split(",")
            for n in numeros:
                if (minimo > int(n)):
                    minimo = int(n)
        maximo = -1;
        return {cantidad, minimo, maximo, 0}


