# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:44:54 2021

@author: qqwdf
"""
from graphviz import Digraph


import pandas as pd

df= pd.read_csv(r'淡江ef-00-3028090-010.csv')

target="父件料品"
X=input("please input target :")
count=input("please input number :")

count=int(count)

print(X,count)
#print(df)
#找父件
def findfather(X):
    a=df[df[target]==X].index.tolist()
    return a
# count=4
####################################################33
f = Digraph('fortheking', filename='fsm.gv')
f.attr(rankdir='LR', size='100,50')
f.attr('node', shape='star')
########################################################

# X="EF-00-3028090-010"
a=findfather(X)
if a ==[]:
    print("None")

def search(a,count,X="9E130-1120-3A2D"):
    
    df.loc[a,"總數量"]=df.loc[a,"總數量"]*count
    
    for row in a:
        print(type(df.loc[row,"總數量"]))
        X=df.iloc[row]["子件料品"]
        temp=findfather(X)
        if temp==[]:
            print('--------------------------------------------------------------')
            print(df.loc[row,["父件料品","子件料品","總數量","階層"]])
            print(df.loc[row,["父件料品"]])
            f.edge(df.iloc[row]["父件料品"],df.iloc[row]["子件料品"])
        else:
            print('--------------------------------------------------------------')
            print(df.loc[row,["父件料品","子件料品","總數量","階層"]])
            f.edge(df.iloc[row]["父件料品"],df.iloc[row]["子件料品"])
            search(temp,count,X)

search(a,count,X)
f.view()