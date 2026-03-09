class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.(prueba)
    """

    def invertir_lista(self, lista):
        resultado = []
        i = len(lista) - 1

        while i >= 0:
            resultado.append(lista[i])
            i -= 1

        return resultado


    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1


    def eliminar_duplicados(self, lista):
        resultado = []

        for elem in lista:
            encontrado = False

            for r in resultado:
                if r == elem and type(r) == type(elem):
                    encontrado = True
                    break

            if not encontrado:
                resultado.append(elem)

        return resultado


    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = 0
        j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1


        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado


    def rotar_lista(self, lista, k):
        if len(lista) == 0:
            return []

        k = k % len(lista)

        parte1 = lista[-k:] if k != 0 else []
        parte2 = lista[:-k] if k != 0 else lista

        return parte1 + parte2


    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1

        suma_total = n * (n + 1) // 2
        suma_lista = 0

        for num in lista:
            suma_lista += num

        return suma_total - suma_lista


    def es_subconjunto(self, conjunto1, conjunto2):
        for elem1 in conjunto1:
            encontrado = False

            for elem2 in conjunto2:
                if elem1 == elem2:
                    encontrado = True
                    break

            if not encontrado:
                return False

        return True


    def implementar_pila(self):
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if len(pila) == 0:
                return None
            return pila.pop()

        def peek():
            if len(pila) == 0:
                return None
            return pila[-1]

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }


    def implementar_cola(self):
        cola = []

        def enqueue(x):
            cola.append(x)

        def dequeue():
            if len(cola) == 0:
                return None
            return cola.pop(0)

        def peek():
            if len(cola) == 0:
                return None
            return cola[0]

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }


    def matriz_transpuesta(self, matriz):
        if len(matriz) == 0:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])

        transpuesta = []

        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)

        return transpuesta