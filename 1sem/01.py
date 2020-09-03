# Defina a função remove_duplicatas, que recebe uma lista e retorna uma nova lista com os mesmos elementos e na mesma ordem, mas sem valores duplicados.

# Entrada da Função
# Lista de valores numéricos.

# Saída da Função
# Lista sem elementos duplicados.

# Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.

# For example:

# Test
# print(remove_duplicatas([1,2,2,3]))
# Result
# [1, 2, 3]
# Test
# print(remove_duplicatas([1,1,1]))
# Result
# [1]
# Test
# print(remove_duplicatas([0,0,1,1,2,2,3,3]))
# Result
# [0, 1, 2, 3]


lista = [0, 0, 1, 1, 2, 2, 3, 3]

def remove_duplicatas(lista):
    lista_final = []
    for elemento in lista:
            if elemento not in lista_final:
                lista_final.append(elemento)
    return lista_final

print(remove_duplicatas(lista))

        
