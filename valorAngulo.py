import math
teta = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(teta))
cos = math.cos(math.radians(teta))
tg = math.tan(math.radians(teta))
print(f'O seno do ângulo {teta} é {sen: .2f}')
print(f'O cosseno do ângulo {teta} é{cos: .2f}')
print(f'A tangente do ângulo {teta} é {tg: .2f}')