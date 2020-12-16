# Uma Árvores Binárias de Busca (ABB) é uma variação da árvore binária que impõe uma ordem entre os elementos armazenados. Efetivamente, todo elemento na subárvore à esquerda não pode ser maior que o armazenado na raiz; e nenhum elemento na subárvore à direita pode ser menor que o da raiz. Claro, essa propriedade se mantém para qualquer subárvore. 

# Faça um programa que leia uma série de números inteiros, os insira em uma árvore binária de busca, e apresente a árvore pronta. Em caso de chaves repetidas, insira na subárvore à esquerda.

# Entrada
# A entrada consiste de uma linha contendo um valor n, indicando quantos dados serão fornecidos, seguida outra linha com de n valores inteiros representando, cada um, o dado a ser armazenado. Insira os dados na ordem dada.

# Saída
# Apresente, em uma linha, a estrutura da árvore no formato de parênteses aninhados.

# Observação
# Os testes são baseados na representação da árvore por parênteses aninhados da seguinte forma: seja uma árvore de raiz a, e filhos b e c então ela é representada por (a (b () ()) (c () ())). Há um espaço entre cada um dos três componentes da descrição de um nó.

# For example:

# Input	Result
# 0
# ()
# 3
# 2 1 3
# (2 (1 () ()) (3 () ()))
# 3
# 1 2 3
# (1 () (2 () (3 () ())))

# def mostra(raiz):
#     print('(', end='')

#     if raiz:
#         print(f'{raiz.dado} ', end='')
#         mostra(raiz.esq)
#         print(' ', end = '')
#         mostra(raiz.dir)

#     print(')', end='')

# raiz = ArvoreBinaria(10, ArvoreBinaria(7), ArvoreBinaria(15))
# mostra(raiz)

class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def insert_tree(node, element):
    if element > node.dado:
        if node.dir:
            insert_tree(node.dir, element)
        else:
            node.dir = ArvoreBinaria(element)
    else:
        if node.esq:
            insert_tree(node.esq, element)
        else:
            node.esq = ArvoreBinaria(element)

def tree_to_str(raiz):
    if raiz == None:
        return '()'
    else:
        return f'({raiz.dado} {tree_to_str(raiz.esq)} {tree_to_str(raiz.dir)})'

n = int(input())
if n != 0:
    values = input().split(' ')

    tree = ArvoreBinaria(values[0])
    for i in range(1, n):
        insert_tree(tree, values[i])
    print(tree_to_str(tree))

else:
    print('()')

#RESPOSTA
# class ABB():
#     def __init__(self, dado=None, esq=None, dir=None):
#         self.dado = dado
#         self.esq = esq
#         self.dir = dir

#     def __str__(self):
#         if self.dado is None:
#             return '()'

#         esq = self.esq if self.esq else '()'
#         dir = self.dir if self.dir else '()'
#         return f'({self.dado} {esq} {dir})'
        
    
#     def add(self, dado):
#         if self.dado is None:
#             self.dado = dado
#         elif self.dado < dado:
#             if not self.dir:
#                 self.dir = ABB()
#             self.dir.add(dado)
#         else:
#             if not self.esq:
#                 self.esq = ABB()
#             self.esq.add(dado)

# raiz = ABB()
# n = int(input())
# if n > 0:
#     for dado in input().split():
#         raiz.add(int(dado))

# print(raiz)