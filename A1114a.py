# Calcule a média dos valores usando iteração
import numpy as np

x = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
media= 0
for i in x:
    divisão = i/x.size
    media += divisão
print(f"A média é: {media}")
    







