# Uma árvore binária (ab) é uma variação da estrutura de dados árvore em que cada nó, além de armazenar um dado, pode ter até duas subárvores. Neste problema, ela é definida na classe ArvoreBinaria que tem como atributos um dado e as subárvores esq e dir. Sabendo que altura de uma árvore é calculada como o tamanho do caminho mais longo da raiz até uma de suas folhas, defina a função altura, que recebe o nó raiz da árvore e retorna sua altura.



# Entrada
# Não há entrada de dados, as árvores estão definidas em memória e a função é chamada automaticamente.



# Saída
# A saída é a altura da árvore, apresentada automaticamente pelo código de teste.



# Observação
# No primeiro exemplo, a árvore de raiz 1 tem dois filhos, 3 e 2, sendo que o último é um nó folha. Por sua vez, 3 tem 4 e 5 como filhos e esse último é um nó folha. O nó 4 tem apenas um filho 6 que é uma folha. O prefixo é de dois caracteres "--" exceto para a raiz. O prefixo é apresentado uma vez para seus filhos ((2\) e 3); duas vezes para seus "netos" (4 e 5) e três vezes para o descendente mais distante 6. Você não precisa implementar a função mostra.

# For example:

# Test	Result
# mostra(raiz)
# print(f'\naltura: {altura(raiz)}')
# 1
# __3
# ____5
# ____4
# ______6
# __2

# altura: 3
# mostra(raiz)
# print(f'\naltura: {altura(raiz)}')
# 2

# altura: 0
# mostra(raiz)
# print(f'\naltura: {altura(raiz)}')
# 3
# __5
# __4
# ____6

# altura: 2
# mostra(raiz)
# print(f'\naltura: {altura(raiz)}')
# 1
# __2
# ____1
# ______2
# ________1
# __________2
# ____________1
# ______________2
# ________________1
# __________________2
# ____________________1
# ______________________2
# ________________________1
# __________________________2
# ____________________________1
# ______________________________2
# ________________________________1
# __________________________________2
# ____________________________________1
# ______________________________________2
# ________________________________________2
# __2
# ____1
# ______2
# ________1
# __________2
# ____________1
# ______________2
# ________________1
# __________________2
# ____________________1
# ______________________2
# ________________________1
# __________________________2
# ____________________________1
# ______________________________2
# ________________________________1
# __________________________________2
# ____________________________________1
# ______________________________________2
# ________________________________________2

# altura: 20

class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def mostra(raiz):
    print('(', end='')

    if raiz:
        print(f'{raiz.dado} ', end='')
        mostra(raiz.esq)
        print(' ', end = '')
        mostra(raiz.dir)

    print(')', end='')

raiz = ArvoreBinaria(10)
mostra(raiz)

def altura_gamb(raiz):
    if raiz == None:
        return -1

    else:

        esqaltura = altura_gamb(raiz.esq)
        diraltura = altura_gamb(raiz.dir)

        if (esqaltura > diraltura):
            return esqaltura+1
        else:
            return diraltura+1

def altura(raiz):
    retorno = altura_gamb(raiz)
    if retorno != -1:
        return retorno
    return 0

print(altura(raiz))

#RESPOSTA
# def altura(raiz):
#     if raiz is None or not (raiz.esq or raiz.dir):
#         return 0

#     return 1 + max(altura(raiz.esq), altura(raiz.dir))