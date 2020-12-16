# Lipporina e Lipporino são gêmeos idênticos que sempre usam roupas iguais! Numa tentativa de conseguir diferenciá-los, Seu Ricardo (pais deles) resolver tomar medidas drásticas e jogar fora as roupas idênticas. Ajude-o a saber quantas são as peças que eles têm duplicadas.

# Entrada
# A entrada consiste de uma linha contendo um número inteiro  1<n≤10000, indicando quantos são as peças de roupa guardadas, seguida de uma linha com n valores, cada um identificando uma peça de roupa. Cada peça é identificada por dois símbolos, uma letra maiúscula e um dígito.

# Saída
# Apresente, em uma linha, a quantidade de peças duplicadas de roupas dos gêmeos.

# For example:

# Input	Result
# 5
# A1 A2 A2 A1 B9
# 2
# 23
# H6 D3 Y7 A1 Z7 M6 Z2 A1 L4 H8 J2 T3 X4 N9 X7 C3 W7 X4 A1 I6 J7 N9 I0
# 4
# 15
# O2 N7 C8 I3 E5 L5 N5 Q6 U1 G9 T0 A8 Z8 K1 U4

number = int(input())
repete = 0
lista = []

for i in range(0, number):
    clothes = input()
    lista.append(clothes)

lista.sort()

for i in range(0, number):
    if lista[i] == lista[i+1]:
        repete += 1
print(repete)