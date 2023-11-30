"""
este código consiste em fazer um menu
onde o usuário insere alguns dados e dependendo
da situação do usuário recebe alguns benefícios

o desafio desse código está em criar funções e 
variáveis globais 

                                        """


# depositar
# sacar
# imprimir saldo
def depositar():
    global ask_money

    ask_money = int(input("quanto você deseja depositar? "))
    ask_money = ask_money + cliente_cadastro


def sacar():
    pass

def imprimir_saldo():
    pass


def main():
    global cliente_cadastro
    while True:
        ask = int(input("1 - cadastrar cliente\n2 - depositar\n3 - sacar\n4 - imprimir saldo\n5 - sair\n"))

        if ask == 1:
            nome = str(input("digite o nome do cliente: "))
            cpf = str(input("digite o cpf do cliente: "))
        
            cliente_cadastro = int(input("qual o tipo o cliente? 1 - normal, 2 - especial: "))
            # normal: 100R$
            # especial: 200R$
            if cliente_cadastro == 1:
                cliente_cadastro = 100

            elif cliente_cadastro == 2:
                cliente_cadastro = 200
    
        elif ask == 2:
            depositar()
        elif ask == 3:
            sacar()
        elif ask == 4:
            imprimir_saldo()
        else:
            break
        print(cliente_cadastro)
        print(nome)
        #print(cpf)
        print(ask_money)
main()
