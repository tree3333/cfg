# file_root=input("请输入文件路径：")
import pandas as pd
import numpy as np
import torch
from data.dataset import testDataset
import models
import torch as t
from torch.utils.data import DataLoader
import tqdm
from utils import _normalizeee
from config import opt
from shuju import shujuchuli__连续_,get_ids_1,shujuchuli__连续_False_train
def write_csv(results,file_name):
    import csv
    with open(file_name,'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','label'])
        writer.writerows(results)
@t.no_grad()  # pytorch>=0.5
def test(**kwargs):
    file_path=shujuchuli__连续_(opt.原始的测试数据路径,opt.处理后的测试数据路径)
    # file_path='./test_False.csv'
    # # 读取数据
    X_mean,X_std=_normalizeee()
    # file_path='/home/summit/桌面/项目/test_False.csv'
    data_test = pd.read_csv(file_path, encoding='big5')
    list1= get_ids_1(file_path)
    del list1[0]
    id__= np.array(list1)

    data_test = data_test.iloc[:, 3:]
    X_ = data_test.to_numpy()

    # label为1的id的数量
    num_ = int(round(len(X_) / 30))
    print("数据长度:", num_)
    # 将每个id数据用数组表示
    x_ = np.empty([num_, 30 * 9], dtype=float)
    for i in range(num_):
        x_[i, :] = X_[30 * i:30 * (i + 1), :].reshape(1, 30 * 9)  # 把矩阵变为一行
    data_ = (x_ - X_mean) / (X_std + 1e-8)
    # print(data_[0])
    data_ = data_.reshape(-1, 30, 9)

    # 将数据变为tensor型
    test_set = data_.astype(float)
    test_set = t.from_numpy(test_set).float()
    test_set=testDataset(test_set,id__)
    test_dataloader = DataLoader(test_set,
                                batch_size=opt.batch_size,
                                shuffle=False,
                                 #若使用GPU，可取消注释
                                # num_workers=4,
                                drop_last=True)

    # configure model
    model = getattr(models, 'Classifier')().eval()
    if opt.load_model_path:
        model.load(opt.load_model_path)
    # model.load_state_dict(torch.load(opt.load_model_path))
    model.to(opt.device)
    results = []
    for ii, (data, path) in tqdm.tqdm(enumerate(test_dataloader)):
        val_input = data.view(opt.batch_size, 1, 30, 9)
        # print(val_input)
        val_input = torch.tensor(val_input, dtype=torch.float32)
        input = val_input.to(opt.device)

        score = model(input)

        # print(score)
        # probability = t.nn.functional.softmax(score, dim=1)[:, 0].detach().tolist()
        # print(probability)
        # test_label = np.argmax(score.cpu().data.numpy(), axis=1)
        test_label = score.max(dim = 1)[1].detach().tolist()
        # for i in probability:
        #     if round(i)==0:
        #         aa+=1


        batch_results = [(path_.item(), probability_) for path_, probability_ in zip(path, test_label)]

        results += batch_results
    write_csv(results, opt.result_file)
    return results
test()
