from aritmetica import MyArray
from myMatrix import MyMatrix
import unittest 

class Pruebas(unittest.TestCase):

    def _listas(self):
        a = [1,2] 
        b = [[1,2],[2,4]] 
        c = [[1,2],[2,4],[2,4]] 
        d = [[[3,4],[6,5]]] 
        e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]] 
        f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]
        g = [[[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3, 4]]]]
        l = [a,b,c,d,e,f,g]
        return l

    def _operaciones(self):
        a = "Hello world" 
        b = "2 + 10 / 2 - 20" 
        c = "(2 + 10) / 2 - 20" 
        d = "3 * (2 + 10) / 2 - 20" 
        e = "(2 + 10) * 3 / 2 - 20" 
        f = "(2 + 10) / (2 - 20) * 3" 
        g = "(2 + 10 / 2 - 20"
        h = "2 + 10 / 2 - 20"
        l = [''.join(x.split()) for x in [a,b,c,d,e,f,g,h]]
        return l
    
    def test_matrix_dimensions(self):
        l = self._listas()
        expected = [1,2,2,3,3,3,4]
        result = []
        for i in l:
            result.append(MyMatrix(i).dimension())
        self.assertEqual(result,expected)
    
    def test_matrix_straight(self):
        l = self._listas()
        expected = [True,True,True,True,False,True,False]
        result = []
        for i in l:
            result.append(MyMatrix(i).straight())
        self.assertEqual(result,expected)

    def test_matrix_compute(self):
        l = self._listas()
        expected = [3,9,15,18,70,74,74]
        result = []
        for i in l:
            result.append(MyMatrix(i).compute())
        self.assertEqual(result,expected)
    
    def test_array_operation(self):
        l = self._operaciones()
        expected = [False,True,True,True,True,True,False,True]
        result = []
        for i in l:
            result.append(MyArray(i).operation())
        self.assertEqual(result,expected)
    
    def test_array_compute(self):
        l = self._operaciones()
        expected = [False,-13,-14,-2,-2,-2,False,-13]
        result = []
        for i in l:
            result.append(MyArray(i).compute())
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)