# Implemente, de forma recursiva, uma função chamada fatorial que recebe um número inteiro n e mostra o valor de n!.

# Entrada
# A entrada consiste de um inteiro 3≤n≤100.

# Saída
# A saída deve ser o valor de n!. Como o número pode ser grande, apresente o resto de sua divisão inteira por 2357.

# Observações
# No terceiro exemplo, 10!=3628800, mas o resultado apresentado é o resto de sua divisão pelo inteiro 2357.

# For example:

# Test	Result
# print(fatorial(3))
# 6
# print(fatorial(6))
# 720
# print(fatorial(10))
# 1377

def fatorial(n):
    if n == 1:
        return 1
    elif n >= 7:
        return ((n*fatorial(n-1))%2357)
    else:
        return n*fatorial(n-1)

# def fatorial(n):
#     return (1 if n < 2 else n * fatorial(n - 1)) % 2357