# Implemente a função divisores, que recebe um número inteiro e retorna todos os seus divisores inteiros (incluindo 1 e ele mesmo) em uma lista.

# Entrada da Função
# Um número inteiro n>0.

# Saída da Função
# Uma lista com todos os divisores desse número

# Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.

# For example:

# Test	
# print(divisores(5))
# Result
# [1, 5]
# Test
# print(divisores(120))
# Result
# [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
# Test
# print(divisores(131))
# Result
# [1, 131]

def divisores(num):
  lista = []
  for element in range(1, num+1):
    if (num % element) == 0:
      lista.append(element)
  return lista