# Todo professor tem um aluno favorito (e vice versa), mas o Prof. Madeira tem um jeito peculiar de escolher o seu: ele sempre escolhe o i-ésimo melhor aluno. O problema é que ele nunca sabe o valor de i para um aluno específico...

# Dados um conjunto de alunos e seus IRAs, ajude o Prof. Madeira a encontrar seu aluno favorito.

# Entrada
# A primeira linha consiste de 2 inteiros, 1≤a,t≤200, onde a  indica a quantidade de alunos e t a quantidade de tentativas que o Prof. Madeira fará. As a linhas seguintes contém, cada uma, o IRA e o nome do aluno, separados por espaço. As n linhas seguintes contém, cada uma, um valor 1≤ti≤a indicando a posição que o Prof. Ladeira quer verificar.

# Saída
# Para caso de teste ti, apresente, em uma linha, o nome do aluno naquela posição e seu IRA (entre parênteses), separados por espaço.

# Observações
# No primeiro exemplo, o aluno de pior IRA é buscado primeiro, seguido da busca pelo melhor aluno. O terceiro caso de teste exemplifica o comportamento do algoritmo de ordenação no caso de IRAs iguais. 

# For example:

# Input	Result
# 3 2
# 2.50 Joao
# 5.00 Maria
# 2.75 Pedro
# 3
# 1
# Joao (2.50)
# Maria (5.00)
# 5 5
# 2.73 Joana Pinto
# 2.32 Fernanda Sousa
# 1.14 Marcos Ladeira
# 1.21 Geraldo Nobrega
# 0.25 Joana Nobrega
# 1
# 2
# 3
# 4
# 5
# Joana Pinto (2.73)
# Fernanda Sousa (2.32)
# Geraldo Nobrega (1.21)
# Marcos Ladeira (1.14)
# Joana Nobrega (0.25)
# 4 4
# 4.36 Fernanda Sousa
# 4.00 Maria Pinto
# 1.85 Fernanda Silva
# 4.00 Maria Ambrosio
# 4
# 3
# 2
# 1
# Fernanda Silva (1.85)
# Maria Ambrosio (4.00)
# Maria Pinto (4.00)
# Fernanda Sousa