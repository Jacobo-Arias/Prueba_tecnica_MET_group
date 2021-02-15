class MyMatrix():

    def __init__(self, matrix):
        self.matrix = matrix
        
    def dimension(self):
        print(self._dimension(self.matrix))

    def straight(self):
        longitudes = self._lists_long(self.matrix)
        
        # si las longitudes en un inico es un entero es porque solo tiene
        # una dimension, al tener una se dice que todas sin iguales
        if type(longitudes) == int:
            print(True)
            return 
        
        tipo = type(longitudes)
        uniform = True
        # va sacando las longitudes de las listas de adentro hacia afuera
        while tipo == list:
            uniform = uniform and self._compare_long(longitudes)
            longitudes = self._lists_long(longitudes)
            tipo = type(longitudes)
        print(uniform)


    def compute(self):
        print(self._compute(self.matrix))

    # Accede a todos los numeros de manera recursiva
    # como si fuera un arbol y lo retorna a una suma
    def _compute(self,entrada):
        total = 0
        if type(entrada) == list:
            for i in entrada:
                total += self._compute(i)
        elif type(entrada) == int:
            return entrada
        return total


    # llega a cada numero y a medida que va bajando de nivel
    # va sumando uno a la profundidad en la que esta el numero
    # al final retorna la profundiad mayor
    def _dimension(self,entrada, deep = 1):
        total = []
        if type(entrada[0]) == list:
            for i in entrada:
                total.append(self._dimension(i, deep=deep+1))
        elif type(entrada[0]) == int:
            return deep
        return max(total)
    

    # saca las longitudes de cada una de las listas mas internas
    # por eso, si en la lista hay más listas sigue bajando
    # si en la lista hay enteros devuelte su longitud
    def _lists_long(self,entrada):
        total = []
        if type(entrada[0]) == list:
            for i in entrada:
                total.append(self._lists_long(i))
        elif type(entrada[0]) == int:
            return len(entrada)
        return total
    

    # en las listas de longidutes están 
    # las dimensiones de las listas que contenían
    # si la mayor longitud es diferente a la menor es porque no son iguales
    # por eso devuelve False
    # el and es para que una vez encontrada un false todo sea false
    def _compare_long(self,longitudes):
        uniform = True
        if type(longitudes[0]) == int:
            if max(longitudes) == min(longitudes):
                return True
            else:
                return False
        
        elif type(longitudes[0]) == list:
            for i in longitudes:
                uniform = uniform and self._compare_long(i)

        return uniform


def menu():
    return input("""Que desea hacer?
                    1. Sacar las dimensiones
                    2. Saber si es matriz uniforme
                    3. La suma de todos los enteros
                    0. Salir
                    : """)

def listas():
    a = [1,2] 
    b = [[1,2],[2,4]] 
    c = [[1,2],[2,4],[2,4]] 
    d = [[[3,4],[6,5]]] 
    e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]] 
    f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]
    g = [[[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3, 4]]]]
    l = [a,b,c,d,e,f,g]
    return l

def main():
    l = listas()
    op = int
    while op != '0':

        op = menu()
        
        if op == '1':
            for i in l:
                print(i)
                MyMatrix(i).dimension()
        
        elif op == '2':
            for i in l:
                print(i)
                MyMatrix(i).straight()
        
        elif op == '3':
            for i in l:
                print(i)
                MyMatrix(i).compute()

if '__main__' == __name__:
    main()