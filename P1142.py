#Crie um dicionário do Python com as seguintes informações do formato chave-valor:
#joao-competicao etc etc. E em seguida peça ao usuário um nome e imprima qual a equipe a pessoa
#participa. Se o nome não existir na lista imprima que o nome não existe.


nome_equipe = {
    "Joao":"Competicao",
    "Carlos": "Desenvolvimento",
    "Patricia": "Competicao",
    "Caio": "Competicao",
    "Leticia": "Gestao"
}
print("Por favor, insira um nome que direi a equipe a qual a pessoa pertence")
nome = str(input("Insira o nome: "))
if nome in nome_equipe:
    print(f"{nome} pertece à equipe {nome_equipe[nome]}! ")
else:
    print(f"{nome} não existe :(")