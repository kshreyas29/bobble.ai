# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:21:35 2020

@author: ASUS
"""
import itertools
import numpy as np
import pandas as pd
import sys
file_name=sys.argv[1]
df=pd.read_csv(file_name,names=["a",'b','c'])
df=df.fillna(value=-99)
row_count=np.array(df.index).shape[0]
arr=df.to_numpy()
lista=arr.tolist()
for i in range(row_count):
    if -99 in lista[i]:
        lista[i].remove(-99)
final_list=["".join(x) for x in itertools.product(*lista)]
print(', '.join(map(str,final_list)))
