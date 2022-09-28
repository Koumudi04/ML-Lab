import numpy as np
import matplotlib.pyplot as plt
x = [2, 9, 5, 5, 3, 7, 1, 8, 6, 2]
y = [69, 98, 82, 77, 71, 84, 55, 94, 84, 64]

def mean(r):
  s = sum(r)
  n = len(r)
  mean = s / n
  return mean
print(mean(x))

def variance(r):
  r_mean = mean(r)
  n = len(r)
  variance = 0
  for i in range(0, len(x)):
    variance += (x[i] - mean(x)) ** 2
  return variance
print(variance(x))

def covariance(x, y):
  x_mean = mean(x)
  y_mean = mean(y)
  n = len(x)
  covariance = 0
  for i in range(0, n):
    covariance += (x[i] - x_mean) * (y[i] - y_mean)
  return covariance
print(covariance(x, y))

def regression_line_coefficients(x, y):
  b1 = covariance(x, y) / variance(x)
  b0 = mean(y) - (b1 * mean(x))
  return b0, b1
  
c, m = regression_line_coefficients(x, y)
print("Regression line: y = ", m, "x+", c)

def myfunc(x):
  return m*x+c
  
#Mean Square Method
def mean_square(x, y):
  ssr = 0
  sst = 0
  y_mean = mean(y)
  n = len(y)
  for i in range(0, n):
    ssr += (myfunc(x[i]) - y_mean) ** 2
    sst += (y[i] - y_mean) ** 2
  r_square = ssr / sst
  return r_square
  
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
accuracy = mean_square(x,y)
print("Accuracy: ", accuracy)
