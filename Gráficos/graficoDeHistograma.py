import matplotlib.pyplot as plt
from random import random
from math import sqrt
mu=100
sigma=15
x=[]
for i in range(10000):
 u = random()-0.5
 if u >=0 :
    x.append(mu + sigma*sqrt(u))
 else:
    x.append(mu - sigma*sqrt(-u))

plt.hist(x, 50, facecolor='g')
plt.xlabel('Resultado')
plt.ylabel('Probabilidade')
plt.title('Histograma do Teste')
plt.grid(True)
plt.show()