# Uma árvore Stern-Brocot é uma forma de organizar frações não negativas irredutíveis nd aonde n,d são primos entre si. Essa árvore pode ser usada para representar qualquer número racional, e sua construção é muito elegante: dadas duas frações n1d1 e  n2d2, basta inserir uma nova fração  n1+n2d1+d2 entre elas. 

# O caso base da árvore são as frações 01,10, portanto pode-se gerar a nova versão: 
# 01,11,10
# A partir disso, podemos repetir o processo e gerar 2 novos itens:
# 01,12,11,21,10
# Repetindo o processo, mais 4 novos itens:
# 01,13,12,23,11,32,21,31,10
# E assim sucessivamente...

# A seguir é mostrado uma representação da geração dos itens em formato de árvore:

# Árvore de Stern-Brocot

# Para definir um número racional, basta definir um caminho na árvore. Se E e D representam, respectivamente, o nó a esquerda e o a direita, um caminho DEDE define que saímos da raiz, pegamos seu filho a direita, deste o filho a esquerda, então o filho a direita e, por fim, o a esquerda. Ou seja,
# DEDE=85
 
# Cada fração é representada por um string distinto! Dada uma representação como um string na árvore de Stern-Brocot, apresente os valores numéricos da fração equivalente.

# Entrada
# A entrada consiste em um inteiro 0<n≤100 indicando quantos strings serão dadas, seguido de n linhas contendo, cada uma, um string descrevendo o caminho. É garantido que nenhum string tem mais de 50 letras.

# Saída
# Para cada string fornecido, apresente uma linha com os valores da fração, conforme os exemplos. Atenção ao espaço entre os operandos e o operador.

# Observações
# As frações do caso base não são consideradas nos testes.

# For example:

# Input	Result
# 1
# DEDE
# 8 / 5
# 2
# ED
# EEEEEEDDDDD
# 2 / 3
# 6 / 37
# 4
# D
# ED
# DED
# EDED
# 2 / 1
# 2 / 3
# 5 / 3
# 5 / 8

#RESPOSTA
N = int(input())

for _ in range(N):
    esq, dir = (0, 1), (1, 0)
    atual = (1, 1)
    for direção in input():
        if direção == 'E':
            atual, dir = (esq[0] + atual[0], esq[1] + atual[1]), atual
        else:
            esq, atual = atual, (dir[0] + atual[0], dir[1] + atual[1])
    print(f'{atual[0]} / {atual[1]}')