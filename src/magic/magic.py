class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
         if n < 0:
            return None
         if n == 0:
            return 0
         if n == 1:
            return 1
         a, b = 0, 1
         for _ in range(2, n + 1):
          a, b = b, a + b
         return b
    
    def secuencia_fibonacci(self, n):
        if n == 0:
            return []
        if n == 1:
            return [0]

        sec = [0, 1]
        while len(sec) < n:
            sec.append(sec[-1] + sec[-2])
        return sec
    
    def es_primo(self, n):

        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    
    def generar_primos(self, n):
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos

       
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []

        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            anterior = triangulo[-1]

            for j in range(len(anterior) - 1):
                fila.append(anterior[j] + anterior[j + 1])

            fila.append(1)
            triangulo.append(fila)

        return triangulo

    def factorial(self, n):
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d) ** potencia for d in digitos)
        return suma == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)

        suma_objetivo = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False

        diag1 = sum(matriz[i][i] for i in range(n))
        diag2 = sum(matriz[i][n - 1 - i] for i in range(n))

        if diag1 != suma_objetivo or diag2 != suma_objetivo:
            return False

        return True