# Calcule o desvio padrão dos valores usando iteração
import numpy as np
x= np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
media = np.mean(x)
somatorio = 0

for i in x:
    imenosmedia = i - media
    somatorio += imenosmedia ** 2

desviopadrao = np.sqrt (somatorio/len(x))

print(f"O desvio padrão é: {desviopadrao}")

