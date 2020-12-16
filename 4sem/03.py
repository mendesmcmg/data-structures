# D. Florinda é trovada por distintos cavalheiros, mas tem certa dificuldade em se lembrar quais lhe agradam mais. Ela é esperta o suficiente para saber que um programa de computador poderia ordená-los conforme suas preferências, facilitando sua vida. Ela também é persuasiva o bastante para lhe convencer a resolver esta tarefa.

# D. Florinda adora dançar e por conta disso definiu que a altura ideal para seu parceiro é de 1,80 m. Seu primeiro critério é encontrar alguém que é o mais próximo possível desta altura, não faz diferença ser um pouco mais alto ou mais baixo. Dentre os candidatos, ela prefere alguém o mais próximo possível de 75 kg, pois seus pés dançantes não aceitam alguém mais pesado. Se houver pretendentes da mesma altura, ela escolhe o mais leve (pisões são inevitáveis!). Se dois ou mais candidatos têm as mesmas características físicas, ordene-os pelo sobrenome (e depois pelo primeiro nome se for necessário desempatar).

# Defina um algoritmo que ordene uma lista de pretendentes conforme os critérios definidos.

# Entrada
# A entrada consiste em um número n de pretendentes, seguido de n linhas contendo, cada uma, o nome e sobrenome do pretendente (cada um com até 50 caracteres), sua altura (em centímetros - valor inteiro) e sua massa (em quilos - valor inteiro). Os valores são separados por um espaço, e é garantido que não há homônimos e que 2≤n≤100.

# Saída
# A saída deve ser a lista dos pretendentes, um por linha, no formato "Sobrenome, Nome" ordenada conforme as preferências de D. Florinda.

# Observações
# O segundo caso de teste tem praticamente todas as condições possíveis.

# For example:

# Input	Result
# 2
# Miguel Rocha 199 138
# Heitor Pereira 200 200
# Rocha, Miguel
# Pereira, Heitor
# 7
# Guido Batista 195 110
# Heitor Tostes 180 75
# Bruno Costa 180 75
# Joao Kleber 180 65
# Rafael Rodrigues 165 110
# Ricardo Neto 170 70
# Juca Carvalho 180 77
# Costa, Bruno
# Tostes, Heitor
# Kleber, Joao
# Carvalho, Juca
# Neto, Ricardo
# Batista, Guido
# Rodrigues, Rafael
# 10
# William Cavalcante 101 152
# Lucas Costa 206 92
# Gabriel Pereira 203 168
# George Santos 228 184
# George Gomes 222 134
# Jack Santos 225 73
# Harry Oliveira 227 170
# Oliver Pereira 221 105
# Lucas Carvalho 130 43
# Thomas Morais 143 112
# Pereira, Gabriel
# Costa, Lucas
# Morais, Thomas
# Pereira, Oliver
# Gomes, George
# Santos, Jack
# Oliveira, Harry
# Santos, George
# Carvalho, Lucas
# Cavalcante, William