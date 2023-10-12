import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,30)
dizi2 = dizi1 ** 2

# (benimFigure,benimEksen) = plt.subplots()

# benimEksen.plot(dizi1,dizi2,color ="#3A95A8")
# benimEksen.plot(dizi2,dizi1,color ="#C96F23")


(yeniFigure,yeniEksen) = plt.subplots()
yeniEksen.plot(dizi1,dizi2 + 2,color ="b",linewidth =1.0,linestyle="-.")
yeniEksen.plot(dizi1,dizi2 + 10,color ="r",linewidth =1.0,linestyle=":")
yeniEksen.plot(dizi1,dizi2 + 20,color ="r",linewidth =1.0,linestyle="--")
yeniEksen.plot(dizi1,dizi2 + 30,color ="#000000",linewidth =1.0,linestyle="--",marker="o",markersize = 4,markerfacecolor="red")

plt.show()