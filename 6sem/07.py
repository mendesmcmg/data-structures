# Um grafo G = (V, A) armazena as informações de um conjunto de vértices e outro de arestas. Defina a classe Grafo que implementa essa estrutura da dados e algumas funcionalidades.

# A classe Grafo deve ter os atributos vertices, que armazena a informação dos vértices e outro arestas, que armazena as relações entre eles. Estes atributos devem ser implementados como o tipo list, tuple ou dict. Cada vértice é definido por um par (id,dado), identificando o vértice e a informação armazenada nele, respectivamente. Cada aresta é definida por um par (ido,idd), identificando os ids dos vértices de origem e destino, respectivamente. A classe deve fornecer os seguintes métodos:

# insere_v(id, dado), que insere um vértice com as informações dadas.
# insere_a(id_o, id_d), que insere uma nova aresta com as informações dadas.
# remove_v(id), que remove o vértice com o id dado, se existir (a remoção de um vértice implica na remoção de todas as arestas relacionadas a ele).
# remove_a(id_o, id_d), que remove uma nova aresta dada, se existir.
# grau_saida, que recebe o id de um vértice e retorna o grau de saída dele, se existir, 0 caso contrário.
# grau_entrada, que recebe o id de um vértice e retornar o grau de entrada dele, se existir, 0 caso contrário.
# alcancavel, que recebe os ids de dois vértices u,v e retorna um booleano indicando se o vértice v pode ser alcançado a partir de u.
# Os métodos de alteração da estrutura serão chamados para executar uma das instruções, como a seguir:

# IV A dado_A insere o vértice com id==A e a informação dadoA no grafo;
# IA A B insere uma aresta do vértice de id==A para o vértice de id==B, se ambos existirem;
# RV A remove o vértice de id==A, se existir, e todas as arestas relacionadas a ele; e
# RA A B remove a aresta do vértice de id==A para o vértice de id==B, se existir.
# Os outros métodos listados serão chamados nos testes.



# Entrada
# Não há leitura de dados, isso é feito automaticamente. A entrada consiste de uma linha contendo o número 0≤n≤100 indicando a quantidade de operações sobre o grafo, seguida de n linhas contendo, cada uma, uma instrução conforme as previstas.



# Saída
# Não há saída de dados, isso é feito automaticamente.



# Observações
# Os casos de teste chamam as funções descritas, verificam a estrutura do grafo gerado e testam as funções grau_saida, grau_entrada e alcancavel. É garantido que há, no máximo, uma aresta para cada par de vértices u,v,u≠v e que não há laços.



# For example:

# Test	Input	Result
# print(grafo.grau_entrada('A'), grafo.grau_saida('A'), grafo.grau_entrada('B'), grafo.grau_saida('B'))
# 4
# IV A VerticeA
# IA B A
# IV B VerticeB
# IA A B
# 0 1 1 0
# print(grafo.grau_saida('A'), grafo.grau_entrada('A'), grafo.grau_saida('B'), grafo.grau_entrada('B'), grafo.grau_saida('C'), grafo.grau_entrada('C'))
# 7
# IV A VerticeA
# IV B VerticeB
# IA A B
# IV C VerticeC
# IA A C
# IA B C
# RV A
# 0 0 1 0 0 1
# print(grafo.alcancavel('C', 'B'), grafo.alcancavel('A', 'C'), grafo.alcancavel('C', 'A'))
# 7
# IV A VerticeA
# IV B VerticeB
# IA A B
# IV C VerticeC
# IA A C
# IA C B
# RA A B

class Grafo():
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def insere_v(self, id_v, info):
        self.vertices[id_v] = info

    def insere_a(self, id_o, id_d):
        if id_o in self.vertices and id_d in self.vertices:
            self.arestas.append((id_o, id_d))

    def remove_v(self, id_v):
        if id_v in self.vertices:
            del self.vertices[id_v]
            self.arestas = list(filter(lambda a: id_v not in a, self.arestas))

    def remove_a(self, id_o, id_v):
        a = (id_o, id_v)
        if a in self.arestas:
            self.arestas.remove(a)

    def grau_saida(self, id_v):
        return sum(1 for a in self.arestas if id_v == a[0])

    def grau_entrada(self, id_v):
        return sum(1 for a in self.arestas if id_v == a[1])

    def alcancavel(self, id_o, id_d):
        rota = []

        if id_o in self.vertices and id_d in self.vertices:
            rota = [id_o]
            pilha = [id_o]
            while pilha:
                vertice = pilha.pop()
                if vertice not in rota:
                    rota.append(vertice)
                    if vertice == id_d:
                        break

                retira_da_pilha = True
                for _, proximo in list(filter(lambda a: vertice == a[0], self.arestas)):
                    if proximo not in rota:
                        pilha.append(proximo)
                        retira_da_pilha = False
                        break
                if retira_da_pilha and pilha:
                    pilha.pop()

        return rota != [] and rota[-1] == id_d