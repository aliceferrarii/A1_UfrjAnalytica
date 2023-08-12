#Faça uma calculadora de soma que recebe dois números entre 0 e 9 e mostre sua
#soma na tela. Verifique se os números de fato estão dentro do intervalo, senão
#peça para escrever novamente até estar correto.

while True:
    print("Por favor, insira dois números entre 0 e 9 para cálculo da média entre eles")
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))
    if  0<=n1 <=9 and 0<=n2 <=9:
        print("A média é: ",(n1+n2)/2)
        break
    else:
        print("Erro")
      
   
      
