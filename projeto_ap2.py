"""
este código pede que o usuário digite alturas variadas e ao final mostra na tela
a menor e maior altura digitada, a média das alturas, e quantas alturas são menores que a média

considerações finais: eu gostei muito de fazer esse código pois no processo eu descobri uma nova forma
de parar um loop infinito: usando o try/except, antes eu usava uma combinação de input/if/else, que era
incoveniente e repetitiva, esse novo método vou levar para minha vida até encontrar outro método mais eficiente

"""

cont = 0
greater = float('-inf')
lesser = float('inf')
soma_media = 0
height_list = []
quant_media = 0

while True:

    try:
        ask = float(input('digite as alturas ou "sair": '))
    
    # saída do loop quando digitar qualquer letra
    except ValueError:
        print("saindo...")
        break
    
    # cont é responsável por contabilizar a média no final do código
    cont += 1

    
    # verificação das alturas maiores e menores
    if ask > greater:
        greater = ask
    
    if ask < lesser:
        lesser = ask

    # --------------

    soma_media = soma_media + ask


    # adicionando à lista
    height_list.append(ask)

# calculando a média
if cont > 0:
    soma_media /= cont

# usando for para contabilizar as alturas menores que a média
for i in height_list:
    if i < soma_media:
        quant_media += 1

# printando os resultados
print("--------")
print(f'a maior altura cadastrada foi: {greater}')
print(f'a menor altura cadastrada foi: {lesser}')
print("--------")
print(f'a média das alturas foi: {round(soma_media, 2)}')
print(f'a quantidade de alturas menores que a média foram: {quant_media}\n')
