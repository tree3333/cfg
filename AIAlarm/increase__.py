import random
from sklearn.neighbors import NearestNeighbors
import numpy as np


class Smote(object):
    """
    SMOTE algorithm implementation.
    Parameters
    ----------
    samples : {array-like}, shape = [n_samples, n_features]
        Training vector, where n_samples in the number of samples and
        n_features is the number of features.
    N : int, optional (default = 50)
        Parameter N, the percentage of n_samples, affects the amount of final
        synthetic samples，which calculated by floor(N/100)*T.
    k : int, optional (default = 5)
        Specify the number for NearestNeighbors algorithms.
    r : int, optional (default = 2)
        Parameter for sklearn.neighbors.NearestNeighbors API.When r = 1, this
        is equivalent to using manhattan_distance (l1), and euclidean_distance
        (l2) for r = 2. For arbitrary p, minkowski_distance (l_r) is used.
    Examples
    --------
      >>> samples = np.array([[3,1,2], [4,3,3], [1,3,4],
                              [3,3,2], [2,2,1], [1,4,3]])
      >>> smote = Smote(N=200)
      >>> synthetic_points = smote.fit(samples)
      >>> print(synthetic_points)
      [[3.31266454 1.62532908 2.31266454]
       [2.4178394  1.5821606  2.5821606 ]
       [3.354422   2.677211   2.354422  ]
       [2.4169074  2.2084537  1.4169074 ]
       [1.86018171 2.13981829 3.13981829]
       [3.68440949 3.         3.10519684]
       [2.22247957 3.         2.77752043]
       [2.3339721  2.3339721  1.3339721 ]
       [3.31504371 2.65752185 2.31504371]
       [2.54247589 2.54247589 1.54247589]
       [1.33577795 3.83211103 2.83211103]
       [3.85206355 3.04931215 3.        ]]
    """

    def __init__(self, N=50, k=5, r=2):
        # 初始化self.N, self.k, self.r, self.newindex
        self.N = N
        self.k = k
        # self.r是距离决定因子
        self.r = r
        # self.newindex用于记录SMOTE算法已合成的样本个数
        self.newindex = 0

    # 构建训练函数
    def fit(self, samples):
        # 初始化self.samples, self.T, self.numattrs
        self.samples = samples
        # self.T是少数类样本个数，self.numattrs是少数类样本的特征个数
        self.T, self.numattrs = self.samples.shape

        # 查看N%是否小于100%
        if (self.N < 100):
            # 如果是，随机抽取N*T/100个样本，作为新的少数类样本
            np.random.shuffle(self.samples)
            self.T = int(self.N * self.T / 100)
            self.samples = self.samples[0:self.T, :]
            # N%变成100%
            self.N = 100

        # 查看从T是否不大于近邻数k
        if (self.T <= self.k):
            # 若是，k更新为T-1
            self.k = self.T - 1

        # 令N是100的倍数
        N = int(self.N / 100)
        # 创建保存合成样本的数组
        self.synthetic = np.zeros((self.T * N, self.numattrs))

        # 调用并设置k近邻函数
        neighbors = NearestNeighbors(n_neighbors=self.k + 1,
                                     algorithm='ball_tree',
                                     p=self.r).fit(self.samples)

        # 对所有输入样本做循环
        for i in range(len(self.samples)):
            # 调用kneighbors方法搜索k近邻
            nnarray = neighbors.kneighbors(self.samples[i].reshape((1, -1)),
                                           return_distance=False)[0][1:]

            # 把N,i,nnarray输入样本合成函数self._populate
            self._populate(N, i, nnarray)

        # 最后返回合成样本self.synthetic
        return self.synthetic

    # 构建合成样本函数
    def _populate(self, N, i, nnarray):
        # 按照倍数N做循环
        for j in range(N):
            # attrs用于保存合成样本的特征
            attrs = []
            # 随机抽取1～k之间的一个整数，即选择k近邻中的一个样本用于合成数据
            nn = random.randint(0, self.k - 1)

            # 计算差值
            diff = self.samples[nnarray[nn]] - self.samples[i]
            # 随机生成一个0～1之间的数
            gap = random.uniform(0, 1)
            # 合成的新样本放入数组self.synthetic
            self.synthetic[self.newindex] = self.samples[i] + gap * diff

            # self.newindex加1， 表示已合成的样本又多了1个
            self.newindex += 1
import pandas as pd
from config import opt

# data1 = pd.read_csv(opt.train_data_root1_原始, encoding='big5')
#
# data1 = data1.iloc[:, 3:]
# # label为1的id的数量
# X_1 = data1.to_numpy()
# num_1 = int(np.floor(len(X_1) / 30))
# print("label为1数据长度:", num_1)
# # label为0的id的数量
# #一个储存一行一个id数据的矩阵
# x_1= np.empty([num_1, 20 *9], dtype = float)
#
#
# #遍历所有label为1的数据
# for i in range(num_1):
#     x_1[i,:]=X_1[20*i:20*(i+1),:].reshape(1,20*9)#把矩阵变为一行
# print(x_1[0].shape)
# a=x_1[0].reshape(1,20,9)
# print(a.shape)
#
# # # 将每个id数据用数组表示
# # data_1 = {}
# # for num in range(num_1):
# #     sample = np.empty([30, 9])
# #     sample = X_1[num * 30:num * 30 + 30]
# #     data_1[num] = sample
# # data_1 = np.array([list(item) for item in data_1.values()])
# # print(data_1.shape)
# # print(data_1[0].shape)
# # samples = np.array([[3,6,1], [4,3,6], [6,2,9],
# #                     [7,4,7], [5,5,4], [2,2,2]])
# # a=data_1[0:10]
# # print(a)
# smote = Smote(N=325)
# synthetic_points = smote.fit(x_1)
# print(synthetic_points.shape)