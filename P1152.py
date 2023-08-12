#Faça um programa que receba um número n e imprima em cada linha k vezes o
#número relativo à linha, usando a função criada na questão anterior para fazer
#a impressão das linhas:

# from P1151 import impressao_numero 
# k = int(input("Insira um numero: "))
# print()
# n = [range(k)]
# def impressao_linhas (k, n):
#     for i in range(1, k+1):
#      print (impressao_numero(k))    
# print(impressao_linhas(k, n))
k = int(input("Insira um numero: "))
from P1151 import impressao_numero

def impressao_linha(k):
    for x in range(1, k+1):
        linha = " "
        for i in range(x):
            n = k
            impressao_numero
        print(linha)
impressao_linha(k)






