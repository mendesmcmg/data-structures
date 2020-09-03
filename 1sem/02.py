# Meses podem ser identificados por números ou pelos próprio nome. 
# Dado um valor inteiro m identificando um mês, indique o nome deste mês do ano.

# Entrada
# A entrada contém uma linha com um valor inteiro 1≤m≤12.

# Saída
# O nome do mês indicado pelo número lido, por extenso e com a primeira letra maiúscula. Use apenas caracteres ASCII.

# For example:

# Input	Result
# 3
# Marco
# 6
# Junho

months = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

entry = int(input())
index = entry - 1

print(f'{months[index]}')