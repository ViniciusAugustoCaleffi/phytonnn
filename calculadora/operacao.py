import math

class Operacao:
    def __init__(self): #construtor
        self.num1 = 0
        self.num2 = 0
    def coletar(self, num1, num2): #criando o metodo coletar
        self.num1 = num1
        self.num2 = num2

    def somar(self,num1, num2):

        self.coletar(num1,num2) #ultilizando o metodo coletar
        return self.num1 + self.num2

    def subtrair(self,num1,num2):

        self.coletar(num1,num2)
        return self.num1 - self.num2

    def multiplicar(self,num1,num2):
        self.coletar(num1,num2)
        return self.num1 * self.num2

    def dividir(self,num1,num2):
        self.coletar(num1,num2)
        if self.num2 <= 0:
            return "Impossivel dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self,num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}  '
        return resultado

    def potencia(self,base,expoente):
        return pow(base,expoente)

    def raiz(self,num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = ""
        for i in range(1, 11, 1):
            msg += F'\n{i}'
        return msg

    def exercicio02(self):

        msg = ""
        for i in range(2,21,2):
            msg += F'\n{i}'
        return msg

    def exercicio03(self):
        msg = ""
        for i in range(1, 101,1):
            msg += F'\n{i}'
        return msg

    def exercicio04(self):
        msg=""
        for i in range(1,51,1):
            if i % 5 == 0:
                msg += F'\n{i}'
        return msg

    def exercicio05(self):
        msg=""
        self.coletar(num1)
        if num1 % 2 == 0:
            msg += F'\n{"este numero é par"}'
        else:
            msg += F'\n{"este numero é impar"}'





