#O mesmo pode ser feito para o desvio padrão, com .std(), máxima e mínima
#com .max() e .min(), al´em de muitos outros métodos.
import numpy as np
x = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
print(f"O desvio padrão é {np.std(x)}")
print(f"A máxima é {np.max(x)}")
print(f"A mínima é {np.min(x)}")