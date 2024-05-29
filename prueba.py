import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('data.csv',sep = ',')
dataframe=pd.DataFrame(csv[{"NOMBRE"}]) 
print(dataframe)