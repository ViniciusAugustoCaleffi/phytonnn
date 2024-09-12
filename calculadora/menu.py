from operacao import Operacao

class  Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1  = 0
        self.num2  = 0

    def mostrarmenu(self):
        print('\n ------ MENU ------\n\n'
              'Escolha uma das opcões abaixo: ' +
              '\n0. sair'+
              '\n1. somar'+
              '\n2. subtrair'+
              '\n3. dividir'+
              '\n4. multiplicar'+
              '\n5. Potencia'+
              '\n6  raiz'+
              '\n7. tabuada'+
              '\n8. Exercicio01' +
              '\n9. Exercicio02'+
              '\n10. Exercicio03'+
              '\n11. Exercicio04')




    def coletar(self):
        self.num1 = int(input('informe o primeiro numero'))
        self.num2 = int(input('informe o segundo numero'))

    def operacao(self):
        while self.opcao !=0:
            self.mostrarmenu()  # Chamando as opcões
            self.opcao = int(input('Escolha uma das opcoes acima: '))
            if self.opcao == 0:
                print('Obrigado!!!')
            if self.opcao == 1:
                self.coletar() #chamando o input por meio do coletar
                print(f'A soma dos números é: {self.opera.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtracao dos numeros digitados é: `{self.opera.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A multiplicação dos numeros digitados é:{self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'A divisao dos numeros digitados é:{self.opera.dividir(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potencia dos numeros digitados é:{self.opera.exercicio01(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz de {self.num1} é :{self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num1} é :{self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada de {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                print(f'Sequencia dos numero é: {self.opera.exercicio01()}')

            elif self.opcao == 9:
                print(f'Sequencia dos numeros é: {self.opera.exercicio02()}')

            elif self.opcao == 10:
                print(f'Sequencia dos numeros é: {self.opera.exercicio03()}')

            elif self.opcao == 11:
                print(f'Sequencia dos numeros é: {self.opera.exercicio04()}')

            elif self.opcao == 12:
                print(f'Sequencia dos numeros é: {self.opera.exercicio05()}')

            else:
                print("Codigo incorreto")
