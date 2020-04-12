# -*- coding: utf-8 -*-
"""PCA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-2PpfC2caoTHYU-5awsvYPEpRNfGmRlc
"""

# Packages 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Machine learning packages
from sklearn import datasets  
#from sklearn.model_selection import StandardScaler
#from sklearn.metrics import accuracy_score
#from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataSet
df=datasets.load_breast_cancer()

print(df.DESCR)

print(df.keys())

X=df.data
y=df.target

#Standardisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# model creation
model=PCA(n_components=2,random_state=42) 
model.fit(X_scaled)

X_pca=model.transform(X_scaled)

print(X_pca.shape,X_scaled.shape)

# Plot dataset 
plt.figure(figsize=(12,8))
plt.scatter(X_pca[:,0],X_pca[:,1],c=y,cmap='viridis')
plt.xlabel('First component')
plt.ylabel('Second component')
plt.show()

