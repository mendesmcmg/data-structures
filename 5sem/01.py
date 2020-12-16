# Uma árvore binária (ab) é uma variação da estrutura de dados árvore em que cada nó, além de armazenar um dado, pode ter até duas subárvores. Neste problema, ela é definida na classe ArvoreBinaria que tem como atributos um dado e as subárvores esq e dir.  Sabendo que o nível de um nó n na árvore é definido pela quantidade de arestas no caminho até n, defina a função mostra_nivel, que recebe o nó raiz da árvore e um nível, e retorna todas as subárvores cujas raízes estão nesse nível.

# Entrada
# Não há entrada de dados, as árvores estão definidas em memória e a função é chamada automaticamente.

# Saída
# Os testes são baseados na representação da árvore por parênteses aninhados da seguinte forma: seja uma árvore de raiz a, e filhos b e c então ela é representada por (a (b () ()) (c () ())). Há um espaço entre cada um dos três componentes da descrição de um nó. 

# Observações
# Não há caso de teste com nivel além da altura da árvore. Os 3 primeiros casos se referem a mesma árvore.

# For example:

# Test	Result
# mostra_nivel(raiz, 0)
# (4 (2 (1 (0 () ()) ()) (3 () ())) (5 () (6 () ())))
# mostra_nivel(raiz, 1)
# (2 (1 (0 () ()) ()) (3 () ()))
# (5 () (6 () ()))
# mostra_nivel(raiz, 2)
# (1 (0 () ()) ())
# (3 () ())
# (6 () ())
# mostra_nivel(raiz, 11)
# (4 (3 (2 (1 () ()) ()) ()) ())

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

raiz = ArvoreBinaria('4', ArvoreBinaria('2', ArvoreBinaria('1'), ArvoreBinaria('0')), ArvoreBinaria('3', ArvoreBinaria('2'), ArvoreBinaria('5')))


def tree_to_str(raiz):
    if raiz == None:
        return '()'
    else:
        return f'({raiz.dado} {tree_to_str(raiz.esq)} {tree_to_str(raiz.dir)})'

def mostra_nivel(raiz, nivel):    
    if raiz == None:
        return
    if nivel == 0:
        print(tree_to_str(raiz))
    else:
        mostra_nivel(raiz.esq, nivel - 1)
        mostra_nivel(raiz.dir, nivel - 1)


mostra_nivel(raiz, 2)

#RESPOSTA
# def mostra(raiz):
#     print('(', end='');

#     if raiz:
#         print(f'{raiz.dado} ', end='')
#         mostra(raiz.esq)
#         print(' ', end='')
#         mostra(raiz.dir)

#     print(')', end='')

# def mostra_nivel(raiz, nivel):
#     if raiz:
#         if nivel == 0:
#             mostra(raiz)
#             print()
#         else:
#             nivel -= 1
#             mostra_nivel(raiz.esq, nivel)
#             mostra_nivel(raiz.dir, nivel)
