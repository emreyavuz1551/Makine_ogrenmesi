import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv("bilkav.com_veriler.csv")

x = veriler.iloc[:,1:4].values # bağimsiz değişken
y = veriler.iloc[:,4:].values # bağimlı değişken

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5,metric="minkowski")

knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.svm import SVC
svs= SVC(kernel="poly")
svs.fit(X_train,y_train)

y_pred = svs.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print("SVS")
print(cm)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)

y_pred = gnb.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print("gnb")
print(cm)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train,y_train)
y_pred = dtc.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print("DTC")
print(cm)


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10,criterion="entropy")
rfc.fit(X_train,y_train)

y_pred = rfc.predict(X_test)
y_proba = rfc.predict_proba(X_test)
cm = confusion_matrix(y_test,y_pred)
print("rfc")
print(cm)
print(y_test)
print(y_proba[:,0])

from sklearn import metrics
fpr, tpr, thold = metrics.roc_curve(y_test,y_proba[:,0],pos_label="e")
print(fpr)
print(tpr)