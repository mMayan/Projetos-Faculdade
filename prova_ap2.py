"""
este código consiste em fazer um menu
onde o usuário insere alguns dados e dependendo
da situação do usuário recebe alguns benefícios

o desafio desse código está em criar funções e 
variáveis globais 

                                        """

saldo_cliente = 0
tipo_cliente = 0  

def depositar():
    global saldo_cliente
    valor = int(input("Quanto você deseja depositar? "))
    saldo_cliente += valor
    print("depósito feito com sucesso!")

def sacar():
    global saldo_cliente
    valor_saque = int(input("Quanto você deseja sacar? "))
    if valor_saque <= saldo_cliente:
        saldo_cliente -= valor_saque
        print("Saque efetuado com sucesso.")
    else:
        print("Saldo insuficiente.")

def imprimir_saldo():
    print(f'O saldo atual é de: R${saldo_cliente}\n')

def main():
    global saldo_cliente, tipo_cliente

    while True:
        ask = int(input("1 - cadastrar cliente\n2 - depositar\n3 - sacar\n4 - imprimir saldo\n5 - sair\n"))

        if ask == 1:
            nome = str(input("Digite o nome do cliente: "))
            cpf = str(input("Digite o CPF do cliente: "))
            tipo_cliente = int(input("Qual o tipo do cliente? 1 - normal, 2 - especial: "))
            
            if tipo_cliente == 1:
                saldo_cliente = 100
            elif tipo_cliente == 2:
                saldo_cliente = 200

        elif ask == 2:
            depositar()
        elif ask == 3:
            sacar()
        elif ask == 4:
            print(f'nome do cliente: {nome}')
            print(f'cpf: {cpf}')
            imprimir_saldo()
        else:
            break

main()
