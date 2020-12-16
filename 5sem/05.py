# No desenvolvimento de um programa que usa árvores, pode ser necessário ou útil a visualização da estrutura. Considere uma árvore em que cada item é definido pela seguinte classe Arvore:

# class Arvore():
#     def __init__(self, dado):
#         self.dado = dado
#         self.filhos = []
# Defina a função mostra que recebe como argumento a raiz de uma árvore e um prefixo, e mostra todos os elementos da árvore, com sua hierarquia claramente definida no formato especificado. Assuma que todo elemento presenta no atributo filhos de um item é também uma Árvore.

# Entrada
# Não há entrada de dados, as árvores estão definidas em memória e os prefixos são definidos nos casos de teste. É garantido que o prefixo não tem mais de 4 caracteres ASCII e que pode ser identificado de forma visual.

# Saída
# Cada caso de teste chama a função gerada para mostrar uma árvore. Apresente o dado de cada elemento da árvore em uma linha, na ordem em que estão armazenados no vetor. Para cada elemento, apresente o prefixo conforme seu nível.

# Observação
# No primeiro exemplo, a árvore de raiz A tem dois filhos, B e C. por sua vez, B tem 3 filhos, D, E e F, que são folhas, e C tem apenas um filho G que também tem apenas um filho, H, que é uma folha. O prefixo é de dois caracteres "--". Não há prefixo para a raiz, ele é apresentado uma vez para seus filhos ((B\) e C); duas vezes para seus "netos" (D, E, F e G) e três vezes para o descendente mais distante H. O segundo exemplo apresenta a mesma árvore, mas com o prefixo de quatro espaços. O terceiro exemplo mostra uma árvore cuja raiz tem 10 folhas como filhos.

# For example:

# Test	Result
# mostra(arvore, '--')
# A
# --B
# ----D
# ----E
# ----F
# --C
# ----G
# ------H
# mostra(arvore1, '    ')
# A
#     B
#         D
#         E
#         F
#     C
#         G
#             H
# mostra(arvore2, '+')
# A
# +B
# +C
# +D
# +E
# +F
# +G
# +H
# +I
# +J
# +K

class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

arvore = Arvore('A')
n1 = Arvore('B')
n2 = Arvore('C')
n3 = Arvore('D')
n4 = Arvore('E')
n5 = Arvore('F')
n6 = Arvore('G')
n7 = Arvore('H')

arvore.filhos.append(n1)
arvore.filhos.append(n2)

n1.filhos.append(n3)
n1.filhos.append(n4)
n1.filhos.append(n5)

n2.filhos.append(n6)

n6.filhos.append(n7)

def mostra_gamb(noh, caracteres, nivel):
  if noh == None:
    return None
  for i in range(0, nivel):
    print(caracteres, end='')
  print(noh.dado)
  
  for filho in noh.filhos:
    mostra_gamb(filho, caracteres, nivel + 1)

def mostra(arvore, caracteres):
  mostra_gamb(arvore, caracteres, 0)

mostra(arvore, '--')
mostra(arvore, '  ')
mostra(arvore, '+')

#RESPOSTA
# def mostra(raiz,  prefixo, nivel=0):
#     print(f'{prefixo * nivel}{raiz.dado}')
#     for f in raiz.filhos:
#         mostra(f, prefixo, nivel + 1)