import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd
data=pd.read_csv("nameoffile.csv")
x = np.array(data)[:,-1]
y = np.array(data)[:,0]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()
