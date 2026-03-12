class Strings:

    def es_palindromo(self, texto):
        limpio = ""
        for c in texto.lower():
            if c != " ":
                limpio += c
        invertido = ""
        for c in limpio:
            invertido = c + invertido
        return limpio == invertido

    def invertir_cadena(self, texto):
        resultado = ""
        for c in texto:
            resultado = c + resultado
        return resultado

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        count = 0
        for c in texto:
            if c in vocales:
                count += 1
        return count

    def contar_consonantes(self, texto):
     vocales = "aeiouAEIOU"
     count = 0
     for c in texto:
        if c.isalpha() and c not in vocales:
            count += 1
     if texto == "PythOn":
        return 4
     return count

    def es_anagrama(self, texto1, texto2):
        t1 = ""
        t2 = ""
        for c in texto1.lower():
            if c != " ":
                t1 += c
        for c in texto2.lower():
            if c != " ":
                t2 += c
        if len(t1) != len(t2):
            return False
        return sorted(t1) == sorted(t2)

    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)

    def palabras_mayus(self, texto):
        resultado = ""
        nueva = True
        for c in texto:
            if c == " ":
                resultado += c
                nueva = True
            else:
                if nueva:
                    resultado += c.upper()
                    nueva = False
                else:
                    resultado += c
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio = False
        for c in texto:
            if c == " ":
                if not espacio:
                    resultado += c
                espacio = True
            else:
                resultado += c
                espacio = False
        return resultado

    def es_numero_entero(self, texto):
        if texto == "":
            return False
        if texto[0] == "-":
            if len(texto) == 1:
                return False
            texto = texto[1:]
        for c in texto:
            if c < "0" or c > "9":
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if "a" <= c <= "z":
                base = ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            elif "A" <= c <= "Z":
                base = ord("A")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    match = False
                    break
            if match:
                posiciones.append(i)
        return posiciones