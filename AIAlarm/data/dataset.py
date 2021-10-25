#将数据集封装为dataset
import torch
from torch.utils.data import Dataset
class MyDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if y is not None:
            self.y = torch.LongTensor(y)
    def __len__(self):
        return len(self.x)
    def __getitem__(self, index):
        X = self.x[index]
        Y = self.y[index]
        return X, Y

class testDataset(Dataset):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            if y is not None:
                self.y = y

        def __len__(self):
            return len(self.x)

        def __getitem__(self, index):
            X = self.x[index]
            Y = self.y[index]
            return X, Y

