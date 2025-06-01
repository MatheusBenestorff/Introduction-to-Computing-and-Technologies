import matplotlib.pyplot as plt

x = []
y = []

a = -10.5
while True:
    a = a + 0.5
    if a>10:
        break

    x.append(a)
    y.append(a**2+1)

plt.plot(x,y, 'ks')
plt.title("Função Quadrática")
plt.grid(True)
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()