import pandas as pd
import numpy as np
import matplotlib.pyplot as mtp
data = pd.read_csv("Book1.csv")
print(data)

x = np.array(data.iloc[:,:-1])
y = np.array(data.iloc[:,2])

#Splitting the dataset into training and testing set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.40)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#Fitting the KNN classifier to the training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, accuracy_score
result1 = classification_report(y_test, y_pred)
print("Classifier Report: ", result1)
result2 = accuracy_score(y_test, y_pred)
print("Accuracy: ", result2)
