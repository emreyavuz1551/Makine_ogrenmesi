import numpy as np
import matplotlib.pyplot as plt


yaslistesi = [10,20,20,30,30,40,50,80,90,45]
kiloliste  = [20,30,40,70,70,30,80,90,112,60]

numpyYaslistesi = np.array(yaslistesi)
numpykiloliste = np.array(kiloliste)

plt.plot(numpyYaslistesi,numpykiloliste,"b")
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Kilonun yaşa göre grafiği")
plt.show()