import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 ** 3

# plt.plot(dizi1,dizi2,"g*-")

plt.subplot(1,2,1)
plt.plot(dizi1,dizi2,"r*-")
plt.subplot(1,2,2)  #İkinci grafik çiziliyor
plt.plot(dizi2,dizi1,"b*-")

benimFigure = plt.figure()
figureaxes = benimFigure.add_axes([0.2,0.2,0.9,0.9])
figureaxes.plot(dizi1,dizi2,"g")
figureaxes.set_xlabel("X Ekseni Veri İsmi")
figureaxes.set_ylabel("Y Ekseni Veri İsmi")
figureaxes.set_title("Grafik Başlığı")


plt.show()