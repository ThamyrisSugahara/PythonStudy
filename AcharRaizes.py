#-*- coding: utf-8 -*-
import math  #importando biblioteca para calcular raiz e números complexos

a = int(input("Digite o coeficiente 'a' da equação de segundo grau: "))
b = int(input("Digite o coeficiente 'b': "))
c = int(input("Digite o coeficiente 'c': "))

#utilizando fórmula de Bhaskara

delta = b**2 - 4*a*c 

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a) #função math.sqrt(delta) calcula a raiz de delta
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são {:.2f} e {:.2f}".format(x1, x2)) # .format cria string formatada, onde a parte entre chaves {} será substituída pela especificação atribuida
elif delta == 0:
    x1 = -b / (2*a)
    print("A equação tem uma raiz real: {:.2f}".format(x1))
else:
    real = -b / (2*a)
    imaginario = math.sqrt(-delta) / (2*a)
    print("As raízes da equação são complexas:")
    print("x1 = {:.2f} + {:.2f}i".format(real, imaginario))
    print("x2 = {:.2f} - {:.2f}i".format(real, imaginario))

