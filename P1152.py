#Faça um programa que receba um número n e imprima em cada linha k vezes o
#número relativo à linha, usando a função criada na questão anterior para fazer
#a impressão das linhas:

from P1151 import impressao_numero

k = int(input("Insira um número: "))

def impressao_linha(k):
    for i in range(1, k+1):
        impressao_numero(i)
        print()
impressao_linha(k)


