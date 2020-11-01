# Ramos vai para Python em busca do quadrado perfeito. Um número quadrado é fácil de ser calculado, n⋅n, mas e se seu computador não souber multiplicar? Ha, moleza! Basta usar a fórmula:
# n2=∑i=1n2i−1

# Ora, ora... O valor de um quadrado pode ser perfeitamente calculado por uma soma de elementos que por sua vez pode ser calculada de forma recursiva. Faça isso!

# Entrada
# A entrada consiste de um inteiro 0<n≤800.

# Saída
# Apresente, as situações consideradas em cada chamada recursiva, uma por linha, conforme os exemplos.

# Observações
# No primeiro exemplo, a chamada para n=3 aplica a fórmula e lida com os valores 1,3,5, e calcula o resultado adicionando o valor do primeiro elemento (1) à soma dos demais (3,5). A chamada recursiva à função repete o processo, somando o primeiro elemento  (3) à soma dos demais (5). Por fim, o processo é repetido para o último elemento (5) e os demais (nenhum).

