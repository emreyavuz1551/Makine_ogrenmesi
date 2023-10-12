import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

dataFrame = pd.read_excel("merc.xlsx")

# sbn.pairplot(dataFrame)
y = dataFrame["Fiyat"].values
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=15)

scaler = MinMaxScaler()
a = scaler.fit(x_train)
print(a)