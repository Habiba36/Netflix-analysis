import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
data = pd.read_csv(r'C:\Users\DELL\PycharmProjects\netflix_titles')
data.head(7)
print('row:',data.shape[0])
print('col:',data.shape[1])
print("--------------------------------------------------------------------------------")
data.info()
print("--------------------------------------------------------------------------------")
print(data.describe())
print("--------------------------------------------------------------------------------")
print('MISSING VALUES:')
data.isnull().sum()
data_clean = data.copy()
data_clean=data_clean.dropna()
data_clean.isnull().sum()
data_clean.head(7)
data_clean["date_added"] = pd.to_datetime(data_clean['date_added'])
data_clean.head(7)
data_clean