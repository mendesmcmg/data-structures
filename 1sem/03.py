# Implemente uma função chamada primo que recebe um número inteiro e
# retorna um string dizendo se é ou não um número primo.

# Entrada da Função
# Um número inteiro n≥0.

# Saída da Função
# O string "Primo.", caso n seja primo, "Não primo." caso contrário.

# Observações: Implemente apenas a função, o código de teste se 
#encarrega de ler a entrada, chamar a função e imprimir o resultado.

# For example:

# Test	Result
# print(primo(5))
# Primo.
# print(primo(120))
# Não primo.
# print(primo(131))
# Primo.

def primo(num):
  message = 'Não primo.'
  for element in range(2, num):
      if num > 1:
        if (num % element) == 0:
          break
        else:
          message = 'Primo.'
  return message