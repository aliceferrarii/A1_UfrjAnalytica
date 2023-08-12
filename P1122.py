#Façaa um Programa que peça dois números ao usuário e imprima na tela o maior
#deles ou, caso sejam iguais, imprima ‘Números iguais

print("Por favor, insira dois números")
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
if (n1>n2):
    print (n1, "é maior que", n2)
elif (n2>n1):
    print (n2, "é maior que", n1)
elif (n2 == n1):
    print("Números iguais")