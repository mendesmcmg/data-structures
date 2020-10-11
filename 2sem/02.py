# Faça um programa que leia uma frase do teclado com números e palavras separados por espaço. Seu programa deve separar as palavras e números em duas pilhas, uma somente composta por palavras e outra somente de números. A frase não tem restrição de tamanho.
# Entrada
# Uma frase com palavras e números inteiros.

# Saída
# Duas pilhas, uma de palavras e outra de números.

# For example:

# Input	Result
# 80 cao 20 pegar 70 correr
# Palavras:
# correr
# pegar
# cao
# Numeros:
# 70
# 20
# 80
# Comidas disponiveis: 5 Bananas 10 peras 8 maracujas 7 kiwis 1 cachorro
# Palavras:
# cachorro
# kiwis
# maracujas
# peras
# Bananas
# disponiveis:
# Comidas
# Numeros:
# 1
# 7
# 8
# 10
# 5
# 5 politicos corruptos roubavam 200 milhoes e ninguem abria 1 olho
# Palavras:
# olho
# abria
# ninguem
# e
# milhoes
# roubavam
# corruptos
# politicos
# Numeros:
# 1
# 200
# 5

entrada = input().split()

numeros = []
palavras = []

for palavra in entrada:
  if palavra.isnumeric():
    numeros.append(palavra)
  else:
    palavras.append(palavra)

print('Palavras:')
for item in palavras[::-1]:
  print(item)

print('Numeros:')
for item in numeros[::-1]:
  print(item)