# Em Jarangonhonha todos possuíam quartos extremamente organizados, com exceção Faleiros, um estudante de computação. Faleiros tinha muita preguiça de arrumar suas roupas, por isso todo dia que chegava em casa empilhava suas roupas em cima da cadeira. Um certo dia sua namorada entrou em seu quarto e ficou horrorizada com a situação, e mandou ele arrumar tudo na hora.

# Como ele era um estudante de computação e procrastinava muito, em vez de organizar suas roupas resolveu criar um programa capaz de mostrar a ordem que as roupas iriam ficam dentro das gavetas, assim como o tempo necessário para organizar tudo. Fez tudo isso para se organizar primeiro, claro.

# Entrada
# A entrada consiste no número de entradas e nas roupas em cima da cadeira na ordem em que foram inseridas. O formato é tipo cor x, onde tipo e cor são duas strings, e x é um inteiro em minutos de quanto tempo se demora para dobrar a roupa. 

# Saída
# A saída consiste nas roupas já dentro da gaveta  na ordem em que foram inseridas, o total de roupas e o tempo total em minutos gasto para guarda-las.

# For example:

# Input	Result
# 5
# camisa verde 1
# calca azul 3
# sobretudo preto 10
# cueca branca 1
# cueca azul 2
# Tipo: cueca Cor: azul
# Tipo: cueca Cor: branca
# Tipo: sobretudo Cor: preto
# Tipo: calca Cor: azul
# Tipo: camisa Cor: verde
# Total de roupas: 5
# Total de tempo: 17
# 4
# Moletom cinza 3
# Chapeu branco 0
# jaqueta verde 4
# jaqueta preta 5
# Tipo: jaqueta Cor: preta
# Tipo: jaqueta Cor: verde
# Tipo: Chapeu Cor: branco
# Tipo: Moletom Cor: cinza
# Total de roupas: 4
# Total de tempo: 12
# 7
# Moletom preto 5
# cueca azul 2
# cueca cinza 2
# meia branca 1
# meia branca 1
# lencol amarelo 10
# edredom azul 15
# Tipo: edredom Cor: azul
# Tipo: lencol Cor: amarelo
# Tipo: meia Cor: branca
# Tipo: meia Cor: branca
# Tipo: cueca Cor: cinza
# Tipo: cueca Cor: azul
# Tipo: Moletom Cor: preto
# Total de roupas: 7
# Total de tempo: 36

numero = int(input())

entrada = list()
tipos = list()
cores = list()
tempototal = int()
roupas = list()
coloridas = list()

for contador in range(numero):
  entrada = input().split()
  tipo, cor, tempo = entrada
  tipos.append(tipo)
  cores.append(cor)
  tempototal += int(tempo)

roupas = tipos[::-1]
coloridas = cores[::-1]

for contador in range(numero):
  print(f'Tipo: {roupas[contador]} Cor:{coloridas[contador]}')

print(f'Total de roupas: {numero}')
print(f'Total de tempo: {tempototal}')