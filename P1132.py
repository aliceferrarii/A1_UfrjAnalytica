#Faça um programa que primeiro peça a quantidade de membros da equipe e, em
#seguida, para cada membro, peça o seu nome e imprima na tela uma mensagem
#de boas vindas ‘Olá <nome>, seja bem-vindo!’.

nmembros= int(input("Insira a quantidade de membros da equipe: "))
for i in range(nmembros):
    nome = input(f"Digite o nome do membro {i+1}:")
    print("Olá", nome, "seja bem-vindo!")