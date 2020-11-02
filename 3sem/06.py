# Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯

# Cada valor pode ser definido com valores anteriores, por exemplo Fibonacci de 3 é 2, que é o resultado da soma de Fibonacci de 2 + Fibonacci de 1.

# Implemente uma função recursiva chamada fibonacci que recebe como parâmetro um valor n e retorne o n-ésimo elemento da Sequência de Fibonacci.

# Entrada
# Não há entrada de dados, o teste chama a função para um valor inteiro 0≤n≤30.

# Saída
# A saída deve conter uma linha valor do n-ésimo termo da sequência, conforme os exemplos.

# For example:

# Test	Result
# print(fibonacci(0))
# 0
# print(fibonacci(1))
# 1
# print(fibonacci(10))
# 55

listafibo = []
nfibo = 30

def fibonacci(nfibo):

  if nfibo <= 1:
    listafibo[nfibo] = nfibo
    return nfibo
  else:
    listafibo[nfibo] = fibonacci(nfibo-1) + fibonacci(nfibo-2)
    return listafibo[nfibo]

for i in range(nfibo+1):
    listafibo.append(-1)
fibonacci(nfibo)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(10))