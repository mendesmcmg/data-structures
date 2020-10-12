# Você foi contratado pela equipe de desenvolvedores chamada Pós-vida (CEO Fagundes) para programar como deve funcionar o Inferno. A ideia básica é utilizar o tempo das pessoas que lá estão com coisas inúteis. Baseado nisso, você e sua equipe decidiram construir uma fila eterna de pessoas. Essa fila eterna tem o seguinte comportamento: 

# uma pessoa avança na fila quando o primeiro é chamado;
# quando uma pessoa finalmente chega à frente da fila, ela é redirecionada ao fim da fila;
# o processo se repete. 
# Entrada
# A entrada consiste dos nomes das pessoas (somente nomes simples) no estado atual da fila. Esses nomes devem ser separados por espaço. A entrada termina quando um número inteiro positivo X é digitado. Esse número consiste do número de avanços que vão ser feitos na fila.

# Saída
# A saída consiste do nome das pessoas que estão na frente e no fim da fila depois de X avanços. Primeiro é impresso o nome da pessoa que esta na frente e depois o nome da pessoa que esta no fim. Esses nomes são separados por \n.

# For example:

# Input	Result
# Carlos Gabriel Joao Vitor 0
# Pessoa da frente: Carlos
# Pessoa do fim: Vitor
# Carlos Gabriel Joao Vitor 1
# Pessoa da frente: Gabriel
# Pessoa do fim: Carlos
# Carlos Gabriel Joao Vitor 4
# Pessoa da frente: Carlos
# Pessoa do fim: Vitor

lista = input().split()
fila = list()
avanco = 0

for elemento in lista:
  if not elemento.isnumeric():
    fila.append(elemento)
  else:
    avanco = int(elemento)

for contador in range(0, avanco):
  fila.append(fila[0])
  fila.pop(0)

print(f'Pessoa da frente: {fila[0]}')
print(f'Pessoa do fim: {fila[len(fila)-1]}')