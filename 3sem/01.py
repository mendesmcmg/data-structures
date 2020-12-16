# Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯

# A implementação recursiva é interessante, ainda mais quando se quer saber quantas vezes a função Fib é chamada. Faça um programa que apresente esta informação.

# Entrada
# A entrada consiste de um inteiro 0≤n≤30.

# Saída
# Apresente, em uma linha, uma mensagem indicando o valor do n-ésimo termo de Fibonacci e quantas chamadas à função, implementada como descrita no contexto, foram realizadas para chegar a este valor.

# Observações
# No primeiro exemplo, a chamada para n=3 gera duas chamadas, uma para 1 e outra para 2 que, por sua vez, 2 gera mais duas chamadas para 1 e 0, totalizando 5.

# For example:

# Input	Result
# 3
# Fib(3) = 2 (5 chamadas)
# 8
# Fib(8) = 21 (67 chamadas)
 
nfibo = int(input())
counter = 0

def fibonacci(nfibo):
  global counter
  counter += 1
  if (nfibo <= 1):
      return nfibo
  else:
      return fibonacci(nfibo-1) + fibonacci(nfibo-2)
  return counter

print(f'Fib({nfibo}) = {fibonacci(nfibo)} ({counter} chamadas)')

# def Fib(n):
#     if n < 2:
#         return (1, n)
#     chamadas_1, valor_1 = Fib(n - 1)
#     chamadas_2, valor_2 = Fib(n - 2)
    
#     return (1 + chamadas_1 + chamadas_2, valor_1 + valor_2)

# n = int(input())
# chamadas, valor =  Fib(n)