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

    def exercicio05(self,num1):
        self.coletar(self,num1)
        return "par" if num1 % 2 == 0 else "impar"

    def exercicio06(self,num1):
        if num1 > 0:
            return "positivo"
        elif num1 < 0:
            return "negativo"
        else:
            return "zero (0)"

    def exercicio07(self,num1):
            return [(f'{num1} x {i} = {num1 * i}')for i in range(1, 11, 1)]

    def exercicio08(self,num1):
            return list (range (1,num1 + 1))

    def exercicio09(self,num1):
            return sum (range (1,num1 + 1))

    def exercicio10(self,num1):

        self.coletar(self,num1)

        for i in range(2,num1 + 1):

            if (num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0):

                return (num1)

    def exercicio11(self,num1):

        self.coletar(self,num1)

        if num1 % 2 or num1 % 3 or num1 % 5 != 0:

            return "O numero é primo"
        else:

            return "O numero não é primo"

    def exercicio12(self,num1):

        self.coletar(self,num1)

        resultado = math.factorial(num1)

        return (f"O fatorial de {num1} é {resultado}")

    def exercicio13(self):

        num1=5

        fatorial=1

        for i in range(1, num1 + 1):
            fatorial *= i
            if i == 1:
                print(f"{i}")
            else:
                print(f"\n * {i}")

        return fatorial

    def exercicio15(self,num1):
        num1 = input("Digite um número: ")
        num1_str = str(num1)
        soma = 0
        for digito in num1_str:
            soma += int(digito)
        return soma


    def exercicio16(self,num1):

        pares=[i for i in range(1,num1+1) if i % 2 == 0]

        impares=[i for i in range(1,num1+1) if i % 2 !=0]

        return f"pares:  {pares}\n impares: {impares}\n"

    def exercicio17(self,num1):

        self.coletar(self,num1)

        if num1 <= 1:
            return "O número não é primo"
            for i in range(2, int(num1 ** 0.5) + 1):
                if num1 % i == 0:
                    return "O número não é primo"
            return "O número é primo"

