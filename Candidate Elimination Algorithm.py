import pandas as pd
import numpy as np

#read the csv file
data = pd.read_csv("data.csv")
concepts = np.array(data.iloc[:,0:-1])
print("Insatnces are: ", concepts)

#get the target value
target = np.array(data.iloc[:,-1])
print("Target values: ", target)

#defining the function for candidate elimination algorithm
def learn(concepts, target):
  specific_h = concepts[0].copy()
  print("\nInitialization of specific_h and general_h")
  general_h = [["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
  print("\nSpecific boundary:", specific_h)
  print("General boundary: ", general_h)
  for i, h in enumerate(concepts):
    print("\n\nInstance ", i+1, "is", h)
    if target[i] == "Yes":
      print ("Insatance is positive: ")
      for x in range(len(specific_h)):
        if h[x] != specific_h[x]:
          specific_h[x] = '?'
          general_h[x][x] = '?'
    if target[i] == "No":
      print("Instance is negative: ")
      for x in range(len(specific_h)):
        if h[x] != specific_h[x]:
          general_h[x][x] = specific_h[x]
        else:
          general_h[x][x] = '?'
    print("Specific boundary after ", i+1, "Instance is ", specific_h)
    print("General boundary after ", i+1, "Instance is ", general_h)
  indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
  for i in indices:
    general_h.remove(['?', '?', '?', '?', '?', '?'])
  return specific_h, general_h
  
#Get the final values
s_final, g_final = learn(concepts, target)
print("Final specific: ", s_final, sep = "\n")
print("Final general: ", g_final, sep = "\n")
