# Uma árvore binária  é uma variação da estrutura de dados árvore em que cada nó, além de armazenar um dado, pode ter até duas subárvores. Neste problema, ela é definida na classe ArvoreBinaria que tem como atributos um dado e as subárvores esq e dir. Implemente a função comprime que reduz o tamanho de uma determinada árvore que esta pendendo para um dos lados. Essa função tem como argumentos a raiz de uma árvore e o número de rotações a serem realizadas.

# O processo de compressão é simples, dada uma quantidade r de rotações a serem realizadas, basta fazê-las no nó mais a esquerda de cada nível (uma rotação no nível 1, uma no nível 2, e assim sucessivamente até o nível r). 

# Entrada
# Não há entrada de dados, as árvores estão definidas em memória e a função é chamada automaticamente.

# Saída
# A saída é uma árvore binária comprimida, apresentado automaticamente pelo código de teste.

# Observação
# Sua função deve usar a função rotaciona_direita, que já foi implementada, para alterar a estrutura da árvore. Esta função recebe a raiz de uma árvore, executa uma rotação à direita, e retorna a raiz da árvore reestruturada. Os testes são executados em ordem, ou seja, o teste 2 será executado após o teste 1 e assim sucessivamente. É garantido que as árvores testadas estarão desbalanceadas à esquerda. Os testes são baseados na representação da árvore por parênteses aninhados da seguinte forma: seja uma árvore de raiz a, e filhos b e c então ela é representada por (a (b () ()) (c () ())). Há um espaço entre cada um dos três componentes da descrição de um nó. Você não precisa implementar a função mostra.

# For example:

# Test	Result
# raiz = comprime(raiz, 1)
#        Original: (2 (1 () ()) (3 () ()))
# Após compressão: (1 () (2 () (3 () ())))
# raiz = comprime(raiz, 2)
#        Original: (5 (4 (3 (2 (1 () ()) ()) ()) ()) ())
# Após compressão: (4 (2 (1 () ()) (3 () ())) (5 () ()))
# raiz = comprime(raiz, 7)
#        Original: (15 (14 (13 (12 (11 (10 (9 (8 (7 (6 (5 (4 (3 (2 (1 () ()) ()) ()) ()) ()) ()) ()) ()) ()) ()) ()) ()) ()) ()) ())
# Após compressão: (14 (12 (10 (8 (6 (4 (2 (1 () ()) (3 () ())) (5 () ())) (7 () ())) (9 () ())) (11 () ())) (13 () ())) (15 () ()))

#RESPOSTA
# A classe ArvoreBinaria já foi definida.
# A função rotaciona_direita já foi definida.

def comprime(raiz, rotacoes):
    if raiz:
        raiz = rotaciona_direita(raiz)
        
        anterior = raiz
        for _ in range(1, rotacoes):
            anterior.esq = rotaciona_direita(anterior.esq)
            anterior = anterior.esq

    return raiz