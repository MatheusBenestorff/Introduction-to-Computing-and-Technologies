import matplotlib.pyplot as plt
import numpy as np

grupos = 5
media_chico = (9.1, 5.4, 4.0, 7.5, 7.0)
media_joao = (8.6, 6.3, 5.5, 3.5, 5.6)

fig, ax = plt.subplots()
indice = np.arange(grupos)
bar_larg = 0.4
transp = 0.7

plt.bar(indice, media_chico, bar_larg,alpha=transp, color='blue',label='Chico')
plt.bar(indice + bar_larg, media_joao,bar_larg, alpha=transp, color='green',label='João')
plt.xlabel('Matéria')
plt.ylabel('Notas')
plt.title('Notas por pessoa')
plt.xticks(indice + bar_larg, ('Matemática','Português', 'Biologia', 'Física', 'Química'))
plt.legend()
plt.tight_layout()
plt.show()