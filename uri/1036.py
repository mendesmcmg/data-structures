entry = input().split()
a, b, c = entry

a = float(a)
b = float(b)
c = float(c)

if a == 0.0 or (b**2 - 4*a*c) < 0:
    print('Impossivel calcular')
else:
    result1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)  
    result2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print(f'R1 = {result1:.5f}')
    print(f'R2 = {result2:.5f}')