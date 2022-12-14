import numpy as np
import pandas as pd

data = pd.read_csv("knn-aj.csv")
data.head()

dataset = np.array(data)
x = dataset
y = dataset[19]
print("x",x)
print("y", y)

k = 3
ds = []
for i in range(len(x) - 1):
    d = np.subtract(x[i],y)
    t_s = np.square(d)
    rr = np.sum(t_s)
    ds = np.append(ds,[rr])
print("Distances: ", ds)


asd = np.argsort(ds)
print(asd)

wx = sd.count(0)
wy = sd.count(1)
wz = sd.count(2)

if(wx > wy) and (wx > wz):
  print("Species: Iris-setosa")
elif (wy > wz):
  print("Species: Iris-versicolor")
else:
  print("Species: Iris-virginica")
