# Num recanto do Convento Onírico (CO) da UnB, um grupo de alunos resolveu montar um concurso lotérico anual, o πLOTO. Cada aluno tem direito a um único bilhete que contém um número inteiro x entre 1 e 123 (são poucos alunos envolvidos no momento). Na SEMUNI, são sorteados quatro números a, b, c e d e a cada bilhete x gera um número da sorte
# S(x)=|x−a|+|x−b|2+|x−c|3+|x−d|4

# Vence quem tiver o bilhete com o menor número da sorte. Implemente um programa que determina o número do bilhete premiado.

# Entrada
# A entrada contém uma linha com os inteiros 1≤a,b,c,d≤123, separados por um espaço em branco.

# Saída
# Apresente, em uma linha, o número do bilhete vencedor. Se dois ou mais bilhetes geram o número da sorte mínimo, imprima qualquer um deles.

# For example:

# Input	Result
# 1 2 3 4
# 3
# 42 42 42 42
# 42
# 89 43 77 12
# 25