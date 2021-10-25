# coding:utf8
import pandas as pd
import visdom
import torch as t
import time
import torchvision as tv
import numpy as np
from config import opt
from increase__ import Smote
def _normalizeee():
    # 读取数据
    data0 = pd.read_csv(opt.train_data_root0_处理后, encoding='big5')
    data1 = pd.read_csv(opt.train_data_root１_处理后, encoding='big5')

    data1 = data1.iloc[:, 3:]
    if len(data0)>len(data1)*1.5:
        chang = int(len(data1) * 1.5)
    else:chang=len(data0)
    # chang = len(data0)
    data0=data0.iloc[:chang,3:]

    # 划分X
    X_1 = data1.to_numpy()
    X_0 = data0.to_numpy()

    # label为1的id的数量
    num_1 = int(np.floor(len(X_1) / 30))
    num_0 = int(np.floor(len(X_0) / 30))

    x_1 = np.empty([num_1, 30 * 9], dtype=float)
    for i in range(num_1):
        x_1[i, :] = X_1[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行

    data_1 =x_1
    x_0 = np.empty([num_0, 30 * 9], dtype=float)
    for i in range(num_0):
        x_0[i, :] = X_0[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行
    data_0 = x_0.reshape(-1, 30 * 9)
    X = np.concatenate((data_0, data_1), axis=0)
    X_mean, X_std = _normalize(X, train=True)

    data_0 = (data_0 - X_mean) / (X_std + 1e-8)
    data_1 = (data_1 - X_mean) / (X_std + 1e-8)
    data_0 = data_0.reshape(-1, 30, 9)

    data_1 = data_1.reshape(-1, 30, 9)
    return X_mean,X_std

# 以下为作业二代码
def _normalize(X, train=True, specified_column=None, X_mean=None, X_std=None):
    # This function normalizes specific columns of X.
    # The mean and standard variance of training data will be reused when processing testing data.
    #
    # Arguments:
    #     X: data to be processed
    #     train: 'True' when processing training data, 'False' for testing data
    #     specific_column: indexes of the columns that will be normalized. If 'None', all columns
    #         will be normalized.
    #     X_mean: mean value of training data, used when train = 'False'
    #     X_std: standard deviation of training data, used when train = 'False'
    # Outputs:
    #     X: normalized data
    #     X_mean: computed mean value of training data
    #     X_std: computed standard deviation of training data

    if specified_column == None:
        specified_column = np.arange(X.shape[1])
    if train:
        X_mean = np.mean(X[:, specified_column], 0).reshape(1, -1)
        X_std = np.std(X[:, specified_column], 0).reshape(1, -1)

    # X[:, specified_column] = (X[:, specified_column] - X_mean) / (X_std + 1e-8)
    # return X, X_mean, X_std
    return X_mean, X_std


class Visualizer():
    """
    封装了visdom的基本操作，但是你仍然可以通过`self.vis.function`
    调用原生的visdom接口
    """

    def __init__(self, env='default', **kwargs):
        import visdom
        self.vis = visdom.Visdom(env=env, use_incoming_socket=False, **kwargs)

        # 画的第几个数，相当于横座标
        # 保存（’loss',23） 即loss的第23个点
        self.index = {}
        self.log_text = ''

    def reinit(self, env='default', **kwargs):
        """
        修改visdom的配置
        """
        self.vis = visdom.Visdom(env=env,use_incoming_socket=False, **kwargs)
        return self

    def plot_many(self, d):
        """
        一次plot多个
        @params d: dict (name,value) i.e. ('loss',0.11)
        """
        for k, v in d.items():
            self.plot(k, v)

    def img_many(self, d):
        for k, v in d.items():
            self.img(k, v)

    def plot(self, name, y):
        """
        self.plot('loss',1.00)
        """
        x = self.index.get(name, 0)
        self.vis.line(Y=np.array([y]), X=np.array([x]),
                      win=name,
                      opts=dict(title=name),
                      update=None if x == 0 else 'append'
                      )
        self.index[name] = x + 1

    def img(self, name, img_):
        """
        self.img('input_img',t.Tensor(64,64))
        """

        if len(img_.size()) < 3:
            img_ = img_.cpu().unsqueeze(0)
        self.vis.image(img_.cpu(),
                       win=name,
                       opts=dict(title=name)
                       )

    def img_grid_many(self, d):
        for k, v in d.items():
            self.img_grid(k, v)

    def img_grid(self, name, input_3d):
        """
        一个batch的图片转成一个网格图，i.e. input（36，64，64）
        会变成 6*6 的网格图，每个格子大小64*64
        """
        self.img(name, tv.utils.make_grid(
            input_3d.cpu()[0].unsqueeze(1).clamp(max=1, min=0)))

    def log(self, info, win='log_text'):
        """
        self.log({'loss':1,'lr':0.0001})
        """

        self.log_text += ('[{time}] {info} <br>'.format(
            time=time.strftime('%m%d_%H%M%S'),
            info=info))
        self.vis.text(self.log_text, win=win)

    def __getattr__(self, name):
        return getattr(self.vis, name)

# _normalizeee__()