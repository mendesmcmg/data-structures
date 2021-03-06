# Ramos vai para Python em busca do quadrado perfeito. Um número quadrado é fácil de ser calculado, n⋅n, mas e se seu computador não souber multiplicar? Ha, moleza! Basta usar a fórmula:
# n2=∑i=1n2i−1

# Ora, ora... O valor de um quadrado pode ser perfeitamente calculado por uma soma de elementos que por sua vez pode ser calculada de forma recursiva. Faça isso!

# Entrada
# A entrada consiste de um inteiro 0<n≤800.

# Saída
# Apresente, as situações consideradas em cada chamada recursiva, uma por linha, conforme os exemplos.

# Observações
# No primeiro exemplo, a chamada para n=3 aplica a fórmula e lida com os valores 1,3,5, e calcula o resultado adicionando o valor do primeiro elemento (1) à soma dos demais (3,5). A chamada recursiva à função repete o processo, somando o primeiro elemento  (3) à soma dos demais (5). Por fim, o processo é repetido para o último elemento (5) e os demais (nenhum).

# n = int(input())

# def quadrado(n):
#     sum = 0
#     for num in range(1, n):
#         if num == n:
#             print({num})
#         else:
#             sum = 2*num - 1
#             print(f'{num} + soma([{n-sum , sum}])')

# quadrado(n)

# RESPOSTA

# def quadrado(lista):
#     if lista == []:
#         lista = [0]
#     if len(lista) == 1:
#         print(f'{lista[0]}')
#         return lista[0]
#     print(f'{lista[0]} + soma({lista[1:]})')
#     return lista[0] + quadrado(lista[1:])

# n = int(input())
# lista = [2 * x - 1 for x in range(1, n + 1)]
# print(f'---------------\n{n} ** 2 == {quadrado(lista)}')