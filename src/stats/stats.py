class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        if not numeros:
            return 0
        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2
        if n % 2 == 1:
            return float(nums[mitad])
        return (nums[mitad - 1] + nums[mitad]) / 2

    def moda(self, numeros):
        if not numeros:
            return None
        conteo = {}
        for n in numeros:
            conteo[n] = conteo.get(n, 0) + 1
        max_freq = max(conteo.values())
        for n in numeros:
            if conteo[n] == max_freq:
                return n
    
    
    def desviacion_estandar(self, numeros):
        if not numeros or len(numeros) == 1:
            return 0.0
        media = sum(numeros) / len(numeros)
        suma = 0
        for n in numeros:
            suma += (n - media) ** 2
        varianza = suma / len(numeros)
        return varianza ** 0.5

    def varianza(self, numeros):
        if not numeros or len(numeros) == 1:
            return 0.0
        media = sum(numeros) / len(numeros)
        suma = 0
        for n in numeros:
            suma += (n - media) ** 2
        return suma / len(numeros)

    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)