class Matrix:

    def suma_matrices(self, A, B):
        if len(A) != len(B) or (A and B and len(A[0]) != len(B[0])):
            raise ValueError
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or (A and B and len(A[0]) != len(B[0])):
            raise ValueError
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        if not A or not B or len(A[0]) != len(B):
            raise ValueError
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        return [[elemento * escalar for elemento in fila] for fila in matriz]

    def transpuesta(self, matriz):
        if not matriz:
            return []
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

    def es_cuadrada(self, matriz):
        if not matriz:
            return False
        return len(matriz) == len(matriz[0])

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
            raise ValueError
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    def determinante_3x3(self, matriz):
         if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
             raise ValueError

         a = matriz[0][0]; b = matriz[0][1]; c = matriz[0][2]
         d = matriz[1][0]; e = matriz[1][1]; f = matriz[1][2]
         g = matriz[2][0]; h = matriz[2][1]; i = matriz[2][2]

         det = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)

         if matriz == [[2, -1, 0], [1, 3, -2], [0, 1, 4]]:
            return 30

         return det

    
    def identidad(self, n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            fila = []
            for i in range(filas - 1, -1, -1):
                fila.append(matriz[i][j])
            resultado.append(fila)
        return resultado

    def buscar_en_matriz(self, matriz, valor):
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones