# Uma palavra foi comprimida para um número inteiro utilizando o seguinte algoritmo:

# Cada letra maiúscula de A até Z foi mapeada para um número entre 1 e 26, sendo a letra A representada pelo número 1, a letra B pelo número 2 e assim por diante.
# O valor da primeira letra da palavra foi colocada nos 5 primeiros bits, os menos significativos, do inteiro, a segunda letra foi colocado nos próximos 5 bits e assim por diante, até a última letra da palavra.
# Depois de colocar cada letra no inteiro os bits restantes do inteiro foram deixados como 0.
# Sua tarefa é recuperar a palavra original, dado o inteiro que a representa. Para isso, implemente uma função recursiva chamada decompress que recebe como argumento o valor inteiro x e retorna a palavra original. 

# Entrada
# Não há entrada de dados, a função é chamada para valores arbitrários definidos nos casos de teste com valores inteiros 0<x.

# Saída
# A função deve retornar um string contendo a palavra original representada pelo inteiro x fornecido à função.

# Observação
# No primeiro exemplo, o valor 65 quando dividido por 2⁵ gera resto 1. Esse valor representa a letra 'A'. O mesmo valor 65 quando feita a divisão inteira por 2⁵ gera valor 2. Portanto, o algoritmo é executado recursivamente. Na segunda execução o resto da divisão de 2 por 2⁵ gera valor 2 representando a letra 'B'. A divisão inteira gera valor zero indicando fim da execução.

# For example:

# Test	Result
# print(decompress(65))
# AB
# print(decompress(54579234))
# BATATA
# print(decompress(6040945729))
# ABACATE

#RESPOSTA
# NUM_BITS = 5

# def letra(numero):
#     # Representação numérica da letra
#     cod_letra = ord('A') + numero - 1
#     # Representação simbólica da letra
#     return chr(cod_letra)

# def decompress(x):
#     if x == 0:
#         return ''
        
#     bits = x % (2 ** NUM_BITS)  # Valor armazenado nos NUM_BITS menos significativos
#     x = x // (2 ** NUM_BITS) # Shift dos bits menos significativos

#     return f'{letra(bits)}{decompress(x)}'

# # Versão com manipulação dos bits
# def decompress(x):
#     if x == 0:
#         return ''

#     bits = x & (2 ** NUM_BITS - 1)
#     x = x >> NUM_BITS

#     return f'{letra(bits)}{decompress(x)}'