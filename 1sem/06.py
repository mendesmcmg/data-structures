# Em um grande campo viviam um coelho e uma raposa. 
# A raposa quer devorar o coelho, enquanto o coelho
# quer fugir da raposa por um dos muitos buracos que 
# possui no campo. Tanto a raposa quanto o coelho não
# são especialistas em matemática, mas também não são
# completamente estúpidos.

# O coelho escolhe um buraco e segue em direção a ele
# em linha reta e a uma velocidade constante. 
# A raposa, que é muito boa em leitura de linguagem 
# corporal, segue no mesmo instante em direção ao 
# mesmo buraco escolhido pelo coelho, em linha reta e
# a uma velocidade igual ao dobro da velocidade do 
# coelho. Se a raposa atinge o buraco primeiro ela 
# devora o coelho, caso contrário o coelho escapa. 
# Seu objetivo é escolher um buraco pelo qual o 
# coelho possa escapar, se tal buraco existir.

# Entrada:
# A entrada consiste de vários casos de teste. 
# A primeira linha de cada caso contém um 
# inteiro n  (0≤n≤1000) que denota o número de buracos
# presentes no campo. A segunda linha apresenta dois 
# números reais, separados por espaço, indicando as 
# coordenadas (x, y) do coelho, e a terceira linha 
# dois valores reais, separados por espaço, com as 
# coordenadas (x, y) da raposa. Na sequência, são 
# apresentadas n linhas, cada uma indicando a posição
# dos buracos no mesmo formato: dois números reais, 
# separados por espaço, com as coordenadas (x, y). 
# Todas as distâncias estão em metros, e sempre −10000≤x,y≤10000.

# Saída:
# Para cada caso, se o coelho puder fugir, a saída 
# deve conter a frase "O coelho pode escapar pelo 
# buraco (x, y)." (atenção ao espaço após a vírgula!),
# indicando as coordenadas exatas do buraco em questão,
# com 3 casas decimais. Caso contrário, a saída deve 
# conter a frase "O coelho não pode escapar."

# Observação:
# Se o coelho puder escapar por mais de um buraco, 
# mostre na saída o buraco que aparece em primeiro 
# lugar na entrada.

# For example:

# Input
# 1 
# 1.000 1.000 
# 2.000 2.000
# 1.500 1.500

# Result
# O coelho nao pode escapar.

# Input
# 2 
# 2.000 2.000 
# 1.000 1.000
# 1.500 1.500
# 2.500 2.500

# Result
# O coelho pode escapar pelo buraco (2.500, 2.500).

import math

num_buracos = int(input())

coelhox, coelhoy = [float(coord) for coord in input().split()]

rapox, rapoy = [float(coord) for coord in input().split()]

escapax = None
escapay = None

for number in range(num_buracos):
  buracox, buracoy = [float(coord) for coord in input().split()]

  distcoe = math.sqrt(((coelhox-buracox)**2) + ((coelhoy-buracoy)**2))
  distrapo = math.sqrt(((rapox-buracox)**2) + ((rapoy-buracoy)**2))

  if distrapo < 2*distcoe:
    if (number >= num_buracos):
      print('O coelho nao pode escapar.')
  elif escapax is None:
    escapax = buracox
    escapay = buracoy
    print(f'O coelho pode escapar pelo buraco ({escapax:.3f}, {escapay:.3f}).')
    break

if escapax is None:
 print('O coelho nao pode escapar.')