# Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯

# Curioso com a Sequência de Fibonacci, onde cada termo subsequente corresponde à soma dos dois anteriores, e os dois primeiros valores da sequência são 0 e 1, dessa vez você resolveu imprimir todos os valores da sequência. Implemente uma função recursiva chamada fibonacci que recebe como parâmetro uma lista vazia e o valor n, e preenche a lista com os n primeiros termos da Sequência.

# Entrada
# Não há entrada de dados, o teste chama a função para um valor inteiro 0≤n≤30.

# Saída
# Não há saída explícita, o teste apresenta a lista resultante de se chamar fibonacci([], n) automaticamente.

# For example:

# Test	Result
# fibonacci(lista, 2)
# print(lista)
# [0, 1]
# fibonacci(lista, 1)
# print(lista)
# [0]
# fibonacci(lista, 10)
# print(lista)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#RESPOSTA
# def fibonacci(lista, n):
#     if len(lista) < n:
#         if len(lista) < 1:
#             lista.append(0)
#         elif len(lista) < 2:
#             lista.append(1)
#         elif len(lista) < n:
#             lista.append(lista[-1] + lista[-2])
#         fibonacci(lista, n)