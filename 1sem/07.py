# No mês de maio você precisa precificar diversos 
# casamentos. Como responsável contábil pela empresa 
# de festas, cabe a você calcular a duração dos eventos de casamento para definir o valor a ser pago. É uma atividade de precisão, portanto é necessário estimar a duração considerando dias, horas, minutos e segundos.

# Crie um programa que calcule a duração total de um 
# evento sabendo o dia, hora, minutos e segundos para
#  as datas inicial e final do mesmo.

# Entrada
# A primeira linha da entrada, contém o dia que começa
# a festa de casamento, seguido de um espaço e do 
# horário exato de início, composto por 3 valores 
# inteiros separados por ':' no formato hh:mm:ss 
# (horas, minutos e segundos, respectivamente). 
# A linha seguinte apresenta, no mesmo formato, a 
# informação da data e horários exatos do fim da 
# festa.

# Saída
# A saída consiste na apresentação da duração do 
# evento, em dias, horas, minutos, e segundos, nesta
# ordem, uma informação por linha. Para cada, indique
# também a unidade de tempo, conforme os exemplos.

# Caso haja um erro e as informações fornecidas na 
# entrada indiquem que o horário de término da festa 
# não é após seu início, indique o erro com a mensagem
# " Data inválida!".

# Input	
# 5 08:12:23
# 9 06:13:23

# Result
# 3 dia(s)
# 22 hora(s)
# 1 minuto(s)
# 0 segundo(s)

# Input	
# 1 2:2:2
# 2 2:2:2

# Result
# 1 dia(s)
# 0 hora(s)
# 0 minuto(s)
# 0 segundo(s)

# Input	
# 8 08:53:12
# 7 08:58:14

# Result
# Data inválida!

initday, inittime = input().split()
finalday, finaltime = input().split()

ihour, imin, isec = inittime.split(':')

fhour, fmin, fsec = finaltime.split(':')

itotal = (int(initday)*86400)+(int(ihour)*3600)+(int(imin)*60)+(int(isec))
ftotal = (int(finalday)*86400)+(int(fhour)*3600)+(int(fmin)*60)+(int(fsec))

if ftotal>itotal:
  duration = int(ftotal-itotal)
  durday = int(duration/86400)
  durhour = int((duration%86400)/3600)
  durmin = int(((duration%86400)%3600)/60)
  dursec = int(((duration%86400)%3600)%60)

  print(f'{durday} dia(s)\n{durhour} hora(s)\n{durmin} minuto(s)\n{dursec} segundo(s)')

else:
  print('Data inválida!')