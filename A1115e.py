#Gere um array de 100 números aleatórios entre 0 e 10 (inclusive) e imprima
#na tela a média, desvio padrão, o maior valor e o menor valor.
from numpy import random
import numpy as np
x = random.randint(11, size=100)
print (f"A média é: {np.mean(x)}")
print (f"O desvio padrão é: {np.std(x)}")
print (f"A máxima é: {np.max(x)}")
print (f"A mínima é: {np.min(x)}")         


 