import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/KSC/sba-project/Subject.csv')


df = df.drop([df.index[2]])


filename = 'Subject1.csv'
df.to_csv(filename, encoding='utf-8-sig', index=False)

