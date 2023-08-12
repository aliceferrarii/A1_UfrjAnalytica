#Faça um programa que peça ao usuário a inserção de dois números e seu 
#programa calculará a média e mostrará o resultado na tela.

print("Por favor, insira dois números para cálculo da média entre eles")
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
média= ((n1+n2)/2)
print( f"A média entre {n1} e {n2} é:", média)
