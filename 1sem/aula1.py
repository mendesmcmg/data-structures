#Cálculos
def calcula_delta(a, b, c):
    return (b ** 2) - (4*a*c)

def calcula_x1(a, b, delta):
    return (-b + (delta ** 0.5)) / (2 * a)

def calcula_x2(a, b, delta):
    return (-b - (delta ** 0.5)) / (2 * a)

#Resultados
def calcula_raizes(a, b, c):
    delta = calcula_delta(a, b, c)

    if delta < 0:
        print('Não há raízes reais')

    if delta == 0:
        x = calcula_x1(a, b, delta)
        print(f'a raiz é {x}')

    if delta > 0:
        x1 = calcula_x1(a, b, delta)
        x2 = calcula_x2(a, b, delta)
        print(f'as raízes são {x1} e {x2}')

#Entrada
a = float(input('Coloque o valor de A: '))
b = float(input('Coloque o valor de B: '))
c = float(input('Coloque o valor de C: '))

calcula_raizes(a, b, c)