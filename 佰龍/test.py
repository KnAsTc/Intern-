# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:16:16 2021

@author: qqwdf
"""

import pandas as pd

df= pd.read_csv(r'DSP2E47.csv')

target="父件"
X=input("please input target :")
count=input("please input number :")

count=int(count)

print(X,count)

#---------------------------------------
#找父件
def findfather(X):
    a=df[df[target]==X].index.tolist()
    return a
a=findfather(X)
target2="p採購件/m自製件"

#print(df["用量"])
c=0
count
def search(a,c,count):
    
    df.loc[a,"用量"]=df.loc[a,"用量"]*count
    
    for row in a:
        if df.iloc[row][target2]!='M':
            print('--------------------------------------------------------------', c)
            print(df.loc[row,["子件","用量"]])
        else:
            X=df.iloc[row]["子件"]
            print('--------------------------------------------------------------', c)
            print(df.loc[row,["子件","用量"]])
            
            count_temp=df.loc[row,"用量"]
            temp=findfather(X)
            search(temp,c+1,count_temp)
            
search(a,c,count)