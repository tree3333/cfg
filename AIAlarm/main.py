import pandas as pd
from increase__ import Smote
import numpy as np
import torch
import models
from shuju import shujuchuli__连续_,shujuchuli__连续_False_train
import torch as t
from data import MyDataset
from torch.utils.data import DataLoader
from torch import nn
from torchnet import meter
import tqdm
from utils import Visualizer,_normalize,_normalizeee
from torch.autograd import Variable
from config import opt
def train():
    # 读取数据
    lr=opt.lr
    # file_path0 = shujuchuli__连续_False_train(opt.train_data_root0_原始,opt.train_data_root0_处理后)
    # file_path1 = shujuchuli__连续_(opt.train_data_root1_原始,opt.train_data_root１_处理后)
    # #
    # # 读取数据
    # data1 = pd.read_csv(file_path1, encoding='big5')
    #
    # data0 = pd.read_csv(file_path0, encoding ='big5')

    # # # 读取数据
    data0 = pd.read_csv('./处理后data___False__长度30.csv', encoding='big5')
    data1 = pd.read_csv('./处理后data___True__长度30.csv', encoding='big5')

    data1=data1.iloc[:,3:]
    if len(data0)>len(data1)*1.5:
        chang = int(len(data1) * 1.5)
    else:chang=len(data0)

    data0=data0.iloc[:chang,3:]
    data00 = data0.iloc[:, 3:].to_numpy()
    # 划分X
    X_1 = data1.to_numpy()
    X_0 = data0.to_numpy()
    print(X_0[0])

    #label为1的id的数量
    num_1=int(np.floor(len(X_1)/30))
    print("label为1数据长度:",num_1)
    #label为0的id的数量
    num_0=int(np.floor(len(X_0)/30))
    print(num_0)
    print("label为0数据长度:",num_0)

    #生成假数据
    # # print(x_1[0].shape)
    # smote = Smote(N=325)
    # synthetic_points = smote.fit(X_1)
    # num_1=int(synthetic_points.shape[0]/30)
    # data_1=synthetic_points

    x_1 = np.empty([num_1, 30 * 9], dtype=float)
    for i in range(num_1):
        x_1[i, :] = X_1[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行
    data_1 = x_1


    x_0 = np.empty([num_0, 30 * 9], dtype=float)
    for i in range(num_0):
        x_0[i, :] = X_0[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行

    data_0 = x_0.reshape(-1, 30*9)
    print(data_0[0].shape)

    X = np.concatenate((data_0, data_1), axis=0)
    X_mean, X_std = _normalize(X, train=True)

    data_0 = (data_0 - X_mean) / (X_std + 1e-8)
    print(X_0[0])
    data_1 = (data_1 - X_mean) / (X_std + 1e-8)
    data_0=data_0.reshape(-1,30,9)
    print(data_0[0].shape)
    data_1 = data_1.reshape(-1, 30, 9)

    #测试集的所占的比例
    detio=0.25
    num_train_detio1= int(len(data_1) * (1 - detio))
    print("训练集的中label为1的部分:",num_train_detio1)
    num_train_detio0= int(len(data_0) * (1 - detio))
    print("训练集的中label为0的部分:",num_train_detio0)

    #拼接训练集数据
    data_train_1=data_1[:num_train_detio1]
    data_train_0=data_0[:num_train_detio0]
    X_train=np.concatenate((data_train_1,data_train_0),axis=0)
    # print(X_train[23])

    data_test_1=data_1[num_train_detio1:]
    data_test_0=data_0[num_train_detio0:]
    X_test=np.concatenate((data_test_1,data_test_0),axis=0)
    # print(X_test[90])

    #创建label
    y_1=np.ones((num_1,))
    y_0=np.zeros((num_0,))
    #拼接训练集label数据
    y_11=y_1[:num_train_detio1,]
    y_01=y_0[:num_train_detio0,]
    Y_train=np.concatenate((y_11,y_01),axis=0)
    print("训练集label Y的形状：",Y_train.shape)
    #拼接测试集label数据
    y_12=y_1[num_train_detio1:,]
    y_02=y_0[num_train_detio0:,]
    Y_test=np.concatenate((y_12,y_02),axis=0)
    print("测试集label Y的形状：",Y_test.shape)

    #将数据变为tensor型
    X_train = X_train.astype(float)
    X_train = t.from_numpy(X_train).float()
    X_test =X_test.astype(float)
    print(X_test.shape)
    X_test = t.from_numpy(X_test).float()

    val_set=MyDataset(X_test,Y_test)
    train_set=MyDataset(X_train,Y_train)
    train_dataloader = DataLoader(train_set,
                                  batch_size =opt.batch_size,
                                  shuffle=True,
                                  num_workers=1,
                                  drop_last=True)

    val_dataloader = DataLoader(val_set,
                                batch_size = opt.batch_size,
                                shuffle=False,
                                num_workers=1,
                                drop_last=True)
    if opt.use_gpu:
        opt.device=t.device('cuda')
    else:
        opt.device = t.device('cpu')

    model = getattr(models,'Classifier')()
    # if opt.load_model_path:
    #     model.load_state_dict(torch.load(opt.load_model_path))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=opt.lr)

    model.to(opt.device)
    loss_meter = meter.AverageValueMeter()
    confusion_matrix = meter.ConfusionMeter(2)
    vis=Visualizer(opt.env)
    previous_loss = 1e10
    abb=[]
    di={}
    for epoch in range(opt.max_epoch):
        loss_meter.reset()
        confusion_matrix.reset()
        for ii, (data_,target) in tqdm.tqdm(enumerate(train_dataloader)):
            # 训练
            data_=data_.reshape(opt.batch_size,1,30,9)
            target=Variable(target)

            target=target.to(opt.device)
            data_ = torch.tensor(data_, dtype = torch.float32)
            data_=Variable(data_)
            data_ = data_.to(opt.device)
            optimizer.zero_grad()
            output= model(data_)
            loss = criterion(output, target.view(-1))
            loss.backward()
            optimizer.step()

            loss_meter.add(loss.item())
            confusion_matrix.add(output.detach(), target.detach())

            # # 可视化
            # if (1 + ii) % opt.print_freq== 0:
            #     vis.plot('loss', loss_meter.value()[0])
        vis.plot('loss', loss_meter.value()[0])
        print(epoch)
        t.save(model.state_dict(), '%s_%s.pth' % (opt.prefix, epoch))
        # validate and visualize
        val_cm, val_accuracy = val(model, val_dataloader)
        cm_value = val_cm.value()
        xu_accuracy = 100. * (cm_value[0][1]) / (cm_value[0][0] + cm_value[0][1])
        lou_accuracy = 100. * (cm_value[1][0]) / (cm_value[1][1] + cm_value[1][0])
        accuracy0=100. * (cm_value[0][0]) / (cm_value[0][0] + cm_value[0][1])
        accuracy1 = 100. * (cm_value[1][1]) / (cm_value[1][1] + cm_value[1][0])
        femshu=accuracy0+accuracy1*1.25
        abb.append(femshu)

        vis.plot('val_accuracy', val_accuracy)
        vis.log("epoch:{epoch},lr:{lr},loss:{loss},train_cm:{train_cm},val_cm:{val_cm},虚警：{xu_accuracy}%,漏警：{lou_accuracy}".format(
            epoch=epoch, loss=loss_meter.value()[0], val_cm=str(val_cm.value()), train_cm=str(confusion_matrix.value()),
            xu_accuracy=xu_accuracy, lou_accuracy=lou_accuracy,
            lr=lr))
        # # update learning rate
        # if loss_meter.value()[0] > previous_loss:
        #     lr = lr * opt.lr_decay
        #     # 第二种降低学习率的方法:不会有moment等信息的丢失
        #     for param_group in optimizer.param_groups:
        #         param_group['lr'] = lr
        # previous_loss = loss_meter.value()[0]
        a=epoch
        if accuracy1>75:
            di.update({a:femshu})

    index=int(max(di,key=di.get))
        # index = abb.index(max(abb))
    model.load_state_dict(torch.load('./checkpoints/modelCNN_0__%s.pth'%(index)))
    print(index)
    t.save(model.state_dict(), '%s_%s.pth' % ('checkpoints/', 'modelmax'))



@t.no_grad()
def val(model,dataloader):
    """
    计算模型在验证集上的准确率等信息
    """
    model.eval()

    confusion_matrix = meter.ConfusionMeter(2)
    for ii, (val_input, label) in tqdm.tqdm(enumerate(dataloader)):
        val_input = val_input.reshape(opt.batch_size, 1, 30, 9)
        val_input = val_input.to(opt.device)
        score = model(val_input)
        confusion_matrix.add(score.detach().squeeze(), label.type(t.LongTensor))

    model.train()
    cm_value = confusion_matrix.value()
    accuracy = 100. * (cm_value[0][0] + cm_value[1][1]) / (cm_value.sum())
    return confusion_matrix, accuracy

@t.no_grad() # pytorch>=0.5
def test():
    vis=Visualizer("asd")
    model = getattr(models,'Classifier')()
    model.load_state_dict(torch.load(opt.load_model_path))
    model.to(opt.device)
    model.eval()
    confusion_matrix = meter.ConfusionMeter(2)
    # 读取数据
    data0 = pd.read_csv(opt.test_data_root0, encoding='big5')
    data1 = pd.read_csv(opt.test_data_root1, encoding='big5')

    data1 = data1.iloc[:, 3:]
    data0 = data0.iloc[:, 3:]
    # 划分X
    X_0 = data0.to_numpy()
    print(X_0[0])
    X_1 = data1.to_numpy()


    # X = np.concatenate((X_0, X_1), axis=0)
    # X_mean, X_std = _normalize(X, train=True)
    #
    # X_0 = (X_0 - X_mean) / (X_std + 1e-8)
    # print(X_0[0])
    # X_1 = (X_1 - X_mean) / (X_std + 1e-8)
    # print(X_0[0])
    # label为1的id的数量
    num_1 = int(np.floor(len(X_1) / 30))
    print("label为1数据长度:", num_1)
    # label为0的id的数量
    num_0 = int(np.floor(len(X_0) / 30))
    print("label为0数据长度:", num_0)
    x_1 = np.empty([num_1, 30 * 9], dtype=float)
    for i in range(num_1):
        x_1[i, :] = X_1[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行
    print(x_1[0].shape)

    x_0 = np.empty([num_0, 30 * 9], dtype=float)
    for i in range(num_0):
        x_0[i, :] = X_0[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行

    X_mean, X_std =_normalizeee()

    data_0 = (x_0 - X_mean) / (X_std + 1e-8)

    data_1 = (x_1 - X_mean) / (X_std + 1e-8)
    data_0 = data_0.reshape(-1, 30, 9)
    print(data_0[0].shape)
    data_1 = data_1.reshape(-1, 30, 9)

    X_test=np.concatenate((data_1,data_0),axis=0)
    # 将数据变为tensor型
    X_test = X_test.astype(float)
    X_test = t.from_numpy(X_test).float()
    y_0=np.zeros(num_0,)
    y_1=np.ones(num_1)
    Y_test=np.concatenate((y_1,y_0),axis=0)
    test_set=MyDataset(X_test,Y_test)


    test_dataloader = DataLoader(test_set,
                                batch_size=opt.batch_size,
                                shuffle=True,
                                num_workers=4,
                                drop_last=True)
    results=[]

    for ii, (val_input, label) in tqdm.tqdm(enumerate(test_dataloader)):
        val_input = val_input.view(opt.batch_size, 1, 30 ,9)
        val_input = torch.tensor(val_input, dtype=torch.float32)
        val_input = val_input.to(opt.device)
        score = model(val_input)
        confusion_matrix.add(score.detach().squeeze(), label.type(t.LongTensor))
        test_label = np.argmax(score.cpu().data.numpy(), axis=1)
        # test_label = score.max(dim = 1)[1].detach().tolist()
        # for i in probability:
        #     if round(i)==0:
        #         aa+=1

        batch_results = [(path_.item(), probability_) for path_, probability_ in zip(label, test_label)]

        results += batch_results
    write_csv(results, opt.result_file)


    cm_value = confusion_matrix.value()
    val_accuracy = 100. * (cm_value[0][0] + cm_value[1][1]) / (cm_value.sum())
    xu_accuracy=100. *  (cm_value[0][1])/(cm_value[0][0] + cm_value[0][1])
    lou_accuracy=100. *  (cm_value[1][0])/(cm_value[1][1] + cm_value[1][0])
    for i in range(10):
        vis.plot('test_accuracy', val_accuracy)
    vis.log("epoch:{epoch},test_cm:{val_cm},虚警：{xu_accuracy}%,漏警：{lou_accuracy}%".format(
        epoch=1, val_cm=str(cm_value), xu_accuracy=xu_accuracy,lou_accuracy=lou_accuracy))

def write_csv(results,file_name):
    import csv
    with open(file_name,'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','label'])
        writer.writerows(results)
if __name__ == '__main__':
  train()