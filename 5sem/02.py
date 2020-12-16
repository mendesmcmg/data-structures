# Uma árvore binária (ab) é uma variação da estrutura de dados árvore em que cada nó, além de armazenar um dado, pode ter até duas subárvores. Neste problema, ela é definida na classe ArvoreBinaria que tem como atributos um dado e as subárvores esq e dir.  Sabendo que o nível de um nó n na árvore é definido pela quantidade de arestas no caminho até n, defina a função nivel, que recebe o nó raiz da árvore e um dado e retorna o nível do dado na árvore. Se não houver nó com valor dado, retorna -1.



# Entrada
# Não há entrada de dados, as árvores estão definidas em memória e a função é chamada automaticamente. É garantido que o valor de n é único, se existir.



# Saída
# A saída é o nível do nó n solicitado, apresentado automaticamente pelo código de teste.



# Observação
# No primeiro exemplo, há 2 arestas no caminho da raiz até 5. No segundo caso, apenas uma. No terceiro exemplo, são 3 arestas. Você não precisa implementar a função mostra.

# For example:

# Test	Result
# mostra(raiz)
# print(f'\nnivel(raiz, {n}): {nivel(raiz, n)}')
# 1
# __3
# ____5
# ____4
# ______6
# __2

# nivel(raiz, 5): 2
# mostra(raiz)
# print(f'\nnivel(raiz, {n}): {nivel(raiz, n)}')
# 1
# __3
# ____5
# ____4
# ______6
# __2

# nivel(raiz, 2): 1
# mostra(raiz)
# print(f'\nnivel(raiz, {n}): {nivel(raiz, n)}')
# 3
# __4
# ____5
# ______6

# nivel(raiz, 6): 3
# print(f'\nnivel(raiz, {n}): {nivel(raiz, n)}')

# nivel(raiz, 42): 5

class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

    # def __str__(self):
    #     if self.dado is None:
    #         return '()'

    #     esq = self.esq if self.esq else '()'
    #     dir = self.dir if self.dir else '()'
    #     return f'({self.dado} {esq} {dir})'

def mostra(raiz):
    print('(', end='')

    if raiz:
        print(f'{raiz.dado} ', end='')
        mostra(raiz.esq)
        print(' ', end = '')
        mostra(raiz.dir)

    print(')', end='')

raiz = ArvoreBinaria(10, ArvoreBinaria(7), ArvoreBinaria(15))
mostra(raiz)

def pega_nivel(raiz, n, nivel):
    if (raiz == None):
        return -1
    
    if (raiz.dado == n):
        return nivel
    
    abaixo = pega_nivel(raiz.esq, n, nivel+1)
    
    if (abaixo != -1):
        return abaixo
    
    abaixo = pega_nivel(raiz.dir, n, nivel+1)
    return abaixo

def nivel(raiz, n):
    return pega_nivel(raiz, n, 0)

print(nivel(raiz, 10))
print(nivel(raiz, 7))
print(nivel(raiz, 15))

#RESPOSTA
# def nivel(raiz, dado):
    # if raiz is None:
    #     return -1
    
    # if raiz.dado == dado:
    #     return 0
    
    # nivel_esq = nivel(raiz.esq, dado)
    # if nivel_esq >= 0:
    #     return 1 + nivel_esq
    
    # nivel_dir = nivel(raiz.dir, dado)
    # if nivel_dir >= 0:
    #     return 1 + nivel_dir

    # return -1