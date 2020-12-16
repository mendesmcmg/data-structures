# O ferreiro Bóris Djoris está ajudando o novo grande empreendimento da sua cidade: um aqueduto para fornecer açaí a todas as residências. Como fornece a tubulação, ele pediu sua ajuda para maximizar os gastos e garantir a alegria da sua galera! A sua tarefa é descobrir o maior gasto possível com a tubulação para conectar todas as residências ao fornecedor. Cada metro de tubulação custa R$ 3.14.



# Entrada
# A primeira linha da entrada indica quantos são as n residências da região (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,d1,v1,d2,v2,⋯,dA,vA, onde id é um inteiro identificando a residência, A é a quantidade de vizinhos de id, e cada vi≠id é um inteiro identificando uma residência vizinha, que está localizada a uma distância de di metros de id.



# Saída
# Apresente o valor total da tubulação que liga todas as residências.



# Observações
# Cada usuário da rede é representado por um id único, todo grafo é não direcionado, conexo e sem laços. Por contrato, você precisa planejar o número mínimo de conexões. No primeiro exemplo, todos os vértices estão ligados entre si, e a tubulação que maximiza o gasto tem 27 metros (R$ 84.78) ligando as residências na seguinte sequência: (1,3) e (3,2). No segundo exemplo, a tubulação que maximiza o gasto tem 709 metros (R$ 2226.26) ligando as residências na seguinte sequência: (2,3),(3,4),(4,6),(6,1) e (6,5).

# For example:

# Input	Result
# 3
# 1 2 6 2 7 3
# 2 2 6 1 20 3
# 3 2 7 1 20 2
# R$ 84.78
# 6
# 5 3 61 4 65 6 51 1
# 4 5 167 3 61 5 22 2 103 1 168 6
# 2 4 66 1 184 3 22 4 43 6
# 3 4 184 2 167 4 13 1 83 6
# 6 5 65 5 125 1 168 4 43 2 83 3
# 1 5 66 2 51 5 125 6 13 3 103 4
# R$ 2226.26
# 4
# 3 2 199 2 63 4
# 1 1 95 2
# 4 1 63 3
# 2 2 95 1 199 3
# R$ 1120.98

vertices, arestas = [], []
for _ in range(int(input())):
    v, A, *vizinhos = input().split()
    vertices.append(int(v))
    for i in range(0, len(vizinhos), 2):
        arestas.append((int(vizinhos[i]), vertices[-1], int(vizinhos[i + 1])))

total = 0
arestas.sort()
agm = {v: set() for v in vertices}
while arestas:  # Kruskal
    t, o, d = arestas.pop()
    if d not in agm[o]:
        agm[o].add(d)
        agm[d].add(o)
        agm[o] |= agm[d]
        agm[d] |= agm[o]
        for v in agm[o]:
            agm[v] |= agm[o]

        total += t

print(f'R$ {total * 3.14:.2f}')
