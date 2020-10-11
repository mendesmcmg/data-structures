# Uma letra significa enqueue e um asterisco significa dequeue na seguinte sequência. 
# Imprima a sequência de carateres retornados pelas operações de dequeue quando esta 
# sequência de operações é realizada em uma  fila inicialmente vazia.

# > ola*** mundo
# ola

# Entrada
# Sequência de caracteres em uma linha.

# Saída
# Sequência de caracteres das operações de dequeue.

# For example:

# Input	Result
# ola*** mundo
# ola
# c > python***
# c >
# rir***,* o brev*******e verb******o *rir****
# rir, o breve verbo rir


palavra = str(input())
final = ""
counter = 0
counter2 = 0

for x in palavra:
  if x == '*':
    counter += 1

for x in palavra:
  if x != '*':
    if counter2 < counter:
      final += x 
      counter2 += 1

print(final)