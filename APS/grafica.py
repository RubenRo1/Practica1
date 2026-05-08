import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("datos.txt")
temperaturas = datos[:,0]
media = datos[:,1]

plt.plot(temperaturas,label="Temperatura")
plt.plot(media,label="Media")
plt.legend()
plt.show()
