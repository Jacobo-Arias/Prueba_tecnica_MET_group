import re


""" La forma utilizando la in-built function eval con try-excep
'la foma pythonista' pero sin expresiones regulares
"""
class MyArray2():
    def __init__(self, entrada):
        self.entrada = entrada
    
    def operation(self):
        print(self._valid())

    def _valid(self):
        try:
            eval(self.entrada)
            return True
        except:
            return False
    
    def compute(self):
        valido = self._valid()
        if valido:
            print(f'{eval(self.entrada)}')
        else:
            print(valido)

class MyArray():
    def __init__(self, entrada):
        self.entrada = entrada
    
    def operation(self):
        print(self._valid())

    def _valid(self):
        expr = '(([0-9]+)[\\+\\-\\*\\/]{1})*((([0-9]+)[\\+\\-\\*\\/]{1}[0-9]+)|\((([0-9]+)[\\+\\-\\*\\/]{1}[0-9]+)\))+([\\+\\-\\*\\/]{1}[0-9]+)*|\(([\\+\\-\\*\\/]{1}[0-9]+)*\)'
        valid = re.match(expr, self.entrada)
        
        if valid:
            return True
        else: 
            return False
    
    def compute(self):
        valid = self._valid()
        if valid:
            # al final opté por evaluarlo igual ya que las in-built functions
            # que vienen con el lenguaje tienden as er mucho más rápidas
            # y óptimas que hacerlo manual
            print(eval(self.entrada))
            return
        else:
            print(valid)
            return

def menu():
    return input("""Que desea hacer?
                    1. Validar operacion
                    2. Calcular operacion
                    0. Salir
                    : """)

def entradas():
    a = "Hello world" 
    b = "2 + 10 / 2 - 20" 
    c = "(2 + 10) / 2 - 20" 
    d = "3 * (2 + 10) / 2 - 20" 
    e = "(2 + 10) * 3 / 2 - 20" 
    f = "(2 + 10) / (2 - 20) * 3" 
    g = "(2 + 10 / 2 - 20"
    h = "2 + 10 / 2 - 20"
    l = [a,b,c,d,e,f,g,h]
    l = [''.join(x.split()) for x in l]
    
    return l

def main():
    l = entradas()
    op = int
    while op != '0':

        op = menu()
        
        if op == '1':
            for i in l:
                print(i, end=' = ')
                MyArray(i).operation()
        
        elif op == '2':
            for i in l:
                print(i, end=' = ')
                MyArray(i).compute()

if '__main__' == __name__:
    main()

    """ Llaamar la calse con el try/excepy y la funcione val """
    # l = entradas()
    # for i in l:
    #     print(i,end=' = ')
    #     MyArray2(i).compute()