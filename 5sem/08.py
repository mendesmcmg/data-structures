# Uma árvore AVL é uma forma de organizar uma árvore binária de modo que esteja sempre balanceada. Para isso, usa uma informação muito simples, para cada nó ela calcula a diferença d entre as alturas de suas subárvores. Para um no R de filhos RE (a esquerda) e RD (a direita), essa diferença é:
# d(R)=altura(RE)−altura(RD)

# Dada uma árvore binária, calcule essas diferenças e apresente a árvore.

# Entrada
# A entrada consiste em uma linha contendo uma árvore representada por parênteses aninhados.

# Saída
# Apresente uma linha com a árvore de diferenças de alturas da árvore fornecida na entrada, também representada por parênteses aninhados.

# Observação
# Os testes são baseados na representação da árvore por parênteses aninhados da seguinte forma: seja uma árvore de raiz a, e filhos b e c então ela é representada por (a (b () ()) (c () ())). Há um espaço entre cada um dos três componentes da descrição de um nó. No terceiro exemplo, d é uma folha, árvore de raiz c está desbalanceada para esquerda, mas as árvores de raízes a,b estão desbalanceadas para a direita.

# For example:

# Input	Result
# (a (b () ()) (c () ()))
# (0 (0 () ()) (0 () ()))
# (a (b (d () ()) (e () ())) (c (f () ()) (g () ())))
# (0 (0 (0 () ()) (0 () ())) (0 (0 () ()) (0 () ())))
# (a () (b () (c (d () ()) ())))
# (-3 () (-2 () (1 (0 () ()) ())))

#RESPOSTA
class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

        h_esq = 0 if esq is None else esq.altura()
        h_dir = 0 if dir is None else dir.altura()
        self.diff_altura = h_esq - h_dir

    def altura(self):
        h_esq = 0 if self.esq is None else self.esq.altura()
        h_dir = 0 if self.dir is None else self.dir.altura()
        return 1 + max(h_esq, h_dir)

    def __str__(self):
        esq = self.esq if self.esq else '()'
        dir = self.dir if self.dir else '()'
        return f'({self.diff_altura} {esq} {dir})'


def parse(arvore_str):
    def split(arvore_str):
        abriu, fechou = 1, 0
        i = 1
        while abriu != fechou:
            if arvore_str[i] == ')':
                fechou += 1
            elif arvore_str[i] == '(':
                abriu += 1
            i += 1
        return arvore_str[:i], arvore_str[i + 1:]  # +1 para remoção do espaço

    if arvore_str == '()':
        return None

    arvore_str = arvore_str[1:-1]  # remoção do parênteses
    raiz, filhos = arvore_str.split(maxsplit=1)
    arvore_esq, arvore_dir = split(filhos)
    return ArvoreBinaria(raiz, parse(arvore_esq), parse(arvore_dir))


arvore_str = input()
print(parse(arvore_str))
