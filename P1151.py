#Crie uma função que recebe um número n e imprima na mesma linha, com
#espaços n vezes o valor.


def impressao_numero (n):
    for x in range(n):
        print(n, end=" ")

if __name__ == "__main__":
    n = int(input("Insira um número: "))
    impressao_numero(n)
