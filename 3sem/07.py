# Você foi convidado para o programa A Xance Única de Brindes do programa  de TV do Caetanão. Esse jogo funciona da seguinte maneira: (1) você vai receber uma lista de possíveis prêmios que poderá ganhar e cada um terá o seu respectivo valor; (2) depois de ver todos os prêmios, Caetanão irá sortear um valor para você; (3) se você conseguir escolher um número de brindes cujo a soma do valor desses brindes seja igual ao valor sorteado, você ganha todos os brindes, senão perde tudo. Como você é um exímio programador e sabe como o jogo funciona, você resolveu implementar um programa para dizer se é possível escolher um conjunto de brindes que o faça ganhar o prêmio ou não.

# Entrada
# A entrada contém 2 linhas. A primeira linha contém n inteiros v onde cada vi indica o valor de um dos prêmios da lista (0≤vi≤100000 e 1≤n≤20). A segunda linha contém um inteiro que indica o número s sorteado por Caetanão (1≤s≤2000000).

# Saída
# A saída deve conter a frase 'E possivel ganhar.', se for possível ganhar os prêmios e 'Impossivel ganhar.' se não for possível ganhar os prêmios.


# For example:

# Input	Result
# 1 2 3 8
# 10
# E possivel ganhar.
# 1 2 3 8
# 7
# Impossivel ganhar.
# 2 2 2 2 5 2 2
# 15
# E possivel ganhar.


brindes = input().split()
preco = input()
lista = list()

def combinar(brindes, lista=[]):

    if len(brindes) == 1:
        return brindes

    for elemento in brindes:
        resto = [i for i in brindes if x != elemento]
        permuta = combinar(resto)

    for item in permuta:
        lista.append([elemento]+ item)

    print(lista)        
    return lista

combinar()

#RESPOSTA
# Como valores possui escopo global, ele está acessível dentro da função verifica
# def verifica(n, premio):

#     if premio == 0:
#         return True
#     elif (n < 0) or (premio < 0):
#         return False
#     else:
#         t1 = verifica(n - 1, premio - valores[n])
#         t2 = verifica(n - 1, premio)

#     return t1 or t2

# valores = [int(s) for s in input().split()]
# premio = int(input())

# if verifica(len(valores)-1, premio) == True:
#     print('E possivel ganhar.')
# else: 
#     print('Impossivel ganhar.')
