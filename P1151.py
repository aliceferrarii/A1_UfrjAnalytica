#Crie uma função que recebe um número n e imprima na mesma linha, com
#espaços n vezes o valor.

n = int(input("Insira um numeroo: "))

def impressao_numero (n):
    for x in range(n):
        print(n, end=" ")
impressao_numero(n)
if __name__ == "__main__": impressao_numero