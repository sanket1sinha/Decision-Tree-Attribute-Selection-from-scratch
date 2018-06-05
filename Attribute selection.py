
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import math as m

k=int(input())
l=[]
while True:
    try:
        matrix=input()
        l.append(matrix)
    except EOFError:
         break   
l=[[i] for i in l]
l1=[]
for i in l:
    a=[words for segments in i for words in segments.split(",")]
    l1.append(a)
cols=l1[0]
content=l1[1:]
df = pd.DataFrame(content)
df.columns = cols
cols=list(df.columns.values)
cols_features=cols[:-1]
col_target=cols[-1]
target_value=df[col_target].unique().tolist()
target_count=df[col_target].value_counts().tolist()
c=0
for i in target_count:
    a=i/len(df)
    b=m.log2(a)
    c=c+a*b
Info_target=c*(-1)
def calculate_info(col_name):
    col_value=df[col_name].unique().tolist()
    col_count=df[col_name].value_counts().tolist()
    li=[]
    for i in col_value:
        f=0
        a=len(df[df[col_name]==i])
        for j in target_value:
            b=len(df[df[col_target]==j])
            c=len(df[(df[col_name]==i)&(df[col_target]==j)])
            if c==0:
                continue
            d=c/a
            e=m.log2(d)
            f=f+d*e
        f=f*(-1)
        g=a/len(df)
        h=f*g
        li.append(h)
    return li
d_info={}
d_gain={}
for i in cols_features:
    li=calculate_info(i)
    fi=sum(li)
    d_info[i] = fi
    g=Info_target-fi
    d_gain[i]=g
print(max(d_gain.items(), key = lambda x: x[1])[0])
d_split={}
for i in cols_features:
    c=0
    tc=df[i].value_counts().tolist()
    for j in tc:
        a=j/len(df)
        b=m.log2(a)
        c=c+a*b
    c=c*(-1)  
    d_split[i]=c
d_gain_ratio={k: d_gain[k]/d_split[k] for k in d_split.keys() & d_gain}
print(max(d_gain_ratio.items(), key = lambda x: x[1])[0])

g=0
for i in target_count:
    a=i/len(df)
    b=a*a
    g=g+b
target_gain=1-g
def calculate_gini(col_name):
    col_value=df[col_name].unique().tolist()
    col_count=df[col_name].value_counts().tolist()
    li=[]
    for i in col_value:
        f=0
        a=len(df[df[col_name]==i])
        for j in target_value:
            b=len(df[df[col_target]==j])
            c=len(df[(df[col_name]==i)&(df[col_target]==j)])
            d=c/a
            e=d*d
            f=f+e
        g=1-f
        h=a/len(df)
        k=g*h
        li.append(k)
    return li
d_gini={}
for i in cols_features:
    li=calculate_gini(i)
    fi=sum(li)
    d_gini[i] = fi
print(min(d_gini.items(), key = lambda x: x[1])[0])

