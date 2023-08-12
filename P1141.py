#Faça um programa cuja primeira linha consiste na seguinte lista:
#competidores = [’Joao’, ’Carlos’, ’Patricia’, ’Caio’, ’Leticia’]
#E em seguida peça ao usuário um nome e imprima uma mensagem dizendo se
#este nome está ou não na lista.

competidores = ["Joao", "Carlos", "Patricia", "Caio", "Leticia"]
nome = input("Por favor, insira um nome: ")
if nome in competidores:
    print("O nome", nome, "está na lista!")
else:
    print("O nome", nome, "não está na lista :(")