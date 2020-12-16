# A ordem de largada da Fórmula 1, é definida no treino classificatório. Os pilotos percorrem o circuito o mais rápido possível, e o tempo da volta é registrado por sensores localizados em três pontos específicos da pista, produzindo as três parciais que, somadas, determinam o tempo da volta.

# Larga na frente o piloto mais rápido, a segunda posição fica com o segundo mais rápido, e assim por diante. Em caso de empate no tempo, o primeiro piloto a ter registrado a marca terá a vantagem. Dados os tempos das três parciais de n pilotos que participaram da classificação, determine o grid de largada da corrida.

# Entrada
# A primeira linha da entrada contém o número 1≤n≤20 de pilotos que participaram do treino classificatório. Na sequência, são fornecidas as informações da melhor volta no treino classificatório para cada piloto, na ordem em que foram registradas. As informações de cada piloto ocupam 2 linhas cada, sendo a primeira delas contém o nome do piloto, formado por uma string de, no máximo, 30 caracteres do alfabeto latino. A segunda linha contém o tempo de cada uma das parciais do piloto, separados por um espaço em branco. O tempo é dado no formato ss:mmm, com 0≤ss≤59 e 0≤mmm≤999.

# Saída
# Apresente o grid de largada, com um piloto por linha. Cada linha deve ter a posição do piloto, seu nome e o tempo da sua volta qualificatória, conforme os exemplos. O tempo de volta deve seguir o formato M:ss.mmm, onde M é dado em minutos, ss em segundos (com dois dígitos) e \texttt{mmm} em milisegundos (com três dígitos).

# Observações
# Atenção ao espaço após a posição no grid e após o nome do piloto.

# For example:

# Input	Result
# 5
# Guilherme
# 20.252 20.654 20.602
# Edison
# 24.000 24.024 23.982
# Caetano
# 20.380 25.816 21.739
# Geraldo
# 20.310 25.725 21.664
# Luis
# 20.289 25.699 21.643
# 1. Guilherme (1:01.508)
# 2. Luis (1:07.631)
# 3. Geraldo (1:07.699)
# 4. Caetano (1:07.935)
# 5. Edison (1:12.006)
# 4
# Nakagima
# 59.999 59.999 59.999
# Blundel
# 59.999 59.999 59.998
# Sato
# 59.999 59.999 59.999
# Salo
# 59.999 59.999 59.998
# 1. Blundel (2:59.996)
# 2. Salo (2:59.996)
# 3. Nakagima (2:59.997)
# 4. Sato (2:59.997)
# 7
# Rosberg
# 20.479 28.888 42.353
# Lauda
# 25.713 30.999 41.989
# Hamilton
# 13.784 20.993 50.919
# Ascari
# 57.148 56.478 19.349
# Fittipaldi
# 59.079 37.093 53.323
# Brabham
# 08.528 57.965 34.357
# Alonso
# 14.876 29.388 42.315
# 1. Hamilton (1:25.696)
# 2. Alonso (1:26.579)
# 3. Rosberg (1:31.720)
# 4. Lauda (1:38.701)
# 5. Brabham (1:40.850)
# 6. Ascari (2:12.975)
# 7. Fittipaldi (2:29.495)
