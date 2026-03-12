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
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        pass
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        pass
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        pass
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        pass