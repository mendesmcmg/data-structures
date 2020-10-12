# Você é um aluno de computação muito ocupado, e por causa disso, está com dificuldades em organizar as suas tarefas. Aproveitando que você  é um aluno aplicado e está dominando os conceitos de fila, implemente um programa que organize as suas atividades por ordem de prioridade.

# Entrada
# Formada por duas linhas. A primeira linha contém a relação de atividades. Cada atividade é formada pelo nome  da tarefa seguido de um numero inteiro Y que representa a prioridade associada a esta atividade (10≤Y≥1). A tarefa de maior prioridade é representada pelo número 1 e a de menor prioridade pelo número 10. A segunda linha contém o valor inteiro (X≥0) que representa a quantidade total de atividades que se pode realizar no período.

# Saída
# A saída consiste do tamanho da fila, seguido da fila em si (com as atividades ainda não cumpridas) ordenada primeiramente em prioridade, seguido por ordem de inserção. Deve seguir o formato:

# Tamanho da fila: %d \n
# Atividade: %s Prioridade: #%d \n
# Observação
# As tarefas que forem cumpridas devem ser removidas da fila. 

# For example:

# Input	Result
# Comer 1 Academia 2 Dormir 3 ElaborarQuestoes 4 Banhar 5 
# 0
# Tamanho da fila: 5
# Atividade: Comer Prioridade: #1
# Atividade: Academia Prioridade: #2
# Atividade: Dormir Prioridade: #3
# Atividade: ElaborarQuestoes Prioridade: #4
# Atividade: Banhar Prioridade: #5
# Academia 5 Compras 4 EstruturaDeDados 1 dormir 8
# 1
# Tamanho da fila: 3
# Atividade: Compras Prioridade: #4
# Atividade: Academia Prioridade: #5
# Atividade: dormir Prioridade: #8
# Comer 1 Academia 2 Dormir 3 ElaborarQuestoes 4 Banhar 5 
# 2
# Tamanho da fila: 3
# Atividade: Dormir Prioridade: #3
# Atividade: ElaborarQuestoes Prioridade: #4
# Atividade: Banhar Prioridade: #5

entrada = input().split()
tamanho = int(input())

result = []
dupla = []

for item in entrada:
  if (len(dupla) == 0):
    dupla.append(item)
  elif (len(dupla) == 1):
    dupla.append(item)
    result.append(dupla)
    dupla = []

result = sorted(result, key=lambda result_entry: result_entry[1]) 

print(f'Tamanho da fila: {len(result)-tamanho}')
for elemento in range(tamanho, len(result)):
  print(f'Atividade: {result[elemento][0]} Prioridade: #{result[elemento][1]}')