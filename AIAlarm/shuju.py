import sys
import pandas as pd
import numpy as np
import csv
from config import opt
# 将大于20行的数据存入csv文件中
def load_useful_data(list,root2):
    valid_data = pd.DataFrame(list)
    valid_data.to_csv(root2)

def get_ids(root):
    # 读取文件
    data = pd.read_csv(root)

    # 将文件的前两行舍去
    data = data.iloc[1:, :]
    # data = data.iloc[:, 1:]
    # 将数据保存为数组
    raw_data = data.to_numpy()
    # 第一行数据
    #print(raw_data[0,:])
    x=len(raw_data)

    ids = []
    # 过滤掉相同的id
    for i in range(0,x-1):
        #读取id
        ids.append(raw_data[i][0])
    ids = np.unique(ids)
    ids = ids.tolist()
    return ids
def get_ids_1(root1):
    # 读取文件
    data = pd.read_csv(root1)
    # 将文件的前两行舍去
    # data = data.iloc[1:, :]
    data = data.iloc[:, 1:]
    # 将数据保存为数组
    raw_data = data.to_numpy()
    # 第一行数据
    #print(raw_data[0,:])
    x=len(raw_data)

    ids = []
    # 过滤掉相同的id
    for i in range(0,x-1):
        #读取id
        ids.append(raw_data[i][0])
    ids = np.unique(ids)
    ids = ids.tolist()
    return ids

def shujuchuli(root1,root2):

    dsadsa=0
    ids=get_ids(root1)
    data = pd.read_csv(root1,index_col=0)
    data = data.iloc[1:, :]
    nbarray = []
    for id in ids:
        total = []
        # 根据id取出对应id的所有数据
        specific_data = data.loc[id]
        specific_data = np.array(specific_data)
        if specific_data.shape[0] >= 30:
            specific_data = specific_data[-30:, ]
            #print(specific_data.shape[0])
            nbarray.extend(specific_data)
            dsadsa+=1
    load_useful_data(nbarray,root2)
    #print(dsadsa)

    return root2

def shujuchuli__连续_(root1,root2):
    iddd = 0
    ids=get_ids(root1)
    data = pd.read_csv(root1,index_col=0)
    data = data.iloc[1:, :]
    nbarray = []
    for id in ids:
        total = []
        # 根据id取出对应id的所有数据
        specific_data = data.loc[id]
        specific_data = np.array(specific_data)
        if specific_data.shape[0] >= 30:
            specific_data = specific_data[-30:,]
            # print(specific_data)
            b=[]
            for m in range(30):
                day=specific_data[m][1]
                day=np.array(day)
                day = day.astype('M8[D]')
                a = day.astype('int32')
                b.append(a)
            # flag = 1
            sum1=0
            for ds in range(29):
                sum = b[ds + 1] - b[ds] - 1
                if (b[ds]+1) != b[ds+1] and sum > 0:
                    sum = b[ds + 1] - b[ds] - 1
                    #print(sum)
                    # if sum<=4:
                    sum = b[ds + 1] - b[ds] - 1
                    bu=np.zeros((sum,11))
                    c=specific_data[:ds+sum1+1]
                    specific_data1=np.concatenate((c,bu),axis=0)
                    specific_data2=specific_data[ds+sum1+1:]
                    specific_data=np.concatenate((specific_data1,specific_data2),axis=0)
                    sum1 += sum
                    # else:
                    #     flag=0
                    #     continue
            # if flag:
            #print(specific_data)
            nbarray.extend(specific_data[-30:])
            iddd +=1
    load_useful_data(nbarray,root2)
    #print(iddd)
    return root2
def shujuchuli__连续_False_train(root1,root2):
    iddd = 0
    ids=get_ids(root1)
    data = pd.read_csv(root1,index_col=0)
    data = data.iloc[1:, :]
    nbarray = []
    for id in ids:
        total = []
        # 根据id取出对应id的所有数据
        specific_data = data.loc[id]
        specific_data = np.array(specific_data)
        if specific_data.shape[0] >= 60:
            specific_data = specific_data[-60:-30,]
            # print(specific_data)
            b=[]
            for m in range(30):
                day=specific_data[m][1]
                day=np.array(day)
                day = day.astype('M8[D]')
                a = day.astype('int32')
                b.append(a)
            # flag = 1
            sum1=0
            for ds in range(29):
                sum = b[ds + 1] - b[ds] - 1
                if (b[ds]+1) != b[ds+1] and sum > 0:
                    sum = b[ds + 1] - b[ds] - 1
                    #print(sum)
                    # if sum<=4:
                    sum = b[ds + 1] - b[ds] - 1
                    bu=np.zeros((sum,11))
                    c=specific_data[:ds+sum1+1]
                    specific_data1=np.concatenate((c,bu),axis=0)
                    specific_data2=specific_data[ds+sum1+1:]
                    specific_data=np.concatenate((specific_data1,specific_data2),axis=0)
                    sum1 += sum
                    # else:
                    #     flag=0
                    #     continue
            # if flag:
            #print(specific_data)
            nbarray.extend(specific_data[-30:])
            iddd +=1
    load_useful_data(nbarray,root2)
    #print(iddd)
    return root2
# a=shujuchuli__连续_('./True_data1.csvdata1.csv','./处理后data___True__长度30.csv')
# a=shujuchuli__连续_False_train('./False_data1.csv','./处理后data___False__长度30.csv')



