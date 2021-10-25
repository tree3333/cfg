import pandas as pd
import numpy as np
dataa=pd.read_csv('/home/summit/桌面/工程/工程/test_False.csv',encoding='big5')

a=range(100,1000)
a=list(a)
# print(a)
# data=[x for x in dataa if　dataa[i] not in a]
b=int(len(dataa))

# data=[dataa[i] for i in range(b) if i not in a ]
tatal=[]
c=dataa[1]
#print(c)

for i in range(b):
    if i not in a:
        tatal.extend(list(dataa[i]))
data=np.array(tatal)
#print(data[0])
