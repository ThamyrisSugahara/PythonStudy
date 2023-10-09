#-*- coding: utf-8 -*-

n = int(input("Digite o número de escalares da lista: ")) #solicitando o número de elementos da lista

lista = [] #[] inicia uma lista vazia para armazenar os escalares

for i in range(n):
    elemento = int(input(f"Digite o elemento {i + 1}: ")) #Solicita um escalar
    # f("..{..}") formatação de string, usando chaves com a variavel dentro
    #= elemento = int(input("Digite o elemento{}".format(i+1)))

    lista.append(elemento) #função que adiciona o elemento escalar à lista

    lista.sort() #vai ordenar em ordem crescente

print("Lista na ordem crescente: ", lista)    