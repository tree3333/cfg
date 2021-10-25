from torch import nn
import numpy as np
import torch
from models.basic_module import BasicModule
class Classifier(BasicModule):
    def __init__(self):
        super(Classifier, self).__init__()
        # torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        # torch.nn.MaxPool2d(kernel_size, stride, padding)
        # input 維度 [1, 30, 9]
        self.dropout = nn.Dropout(p=0.5)
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 64, 3, 1, 1),  # [64, 128, 128]
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, 1, 1),  # [64, 128, 128]
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2, 2, 0),  # [64, 64, 64]

            nn.Conv2d(64, 128, 3, 1, 1),  # [128, 64, 64]
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 128, 3, 1, 1),  # [128, 64, 64]
            nn.BatchNorm2d(128),
            nn.MaxPool2d(2, 2, 0),  # [128, 32, 32]

            nn.Conv2d(128, 256, 3, 1, 1),  # [256, 32, 32]
            nn.BatchNorm2d(256),
            nn.Conv2d(256, 256, 3, 1, 1),  # [256, 32, 32]
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),  # [256, 16, 16]
        )
        self.fc = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256*3*1, 128),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Dropout(),
            # nn.Linear(128, 64),
            # nn.ReLU(),
            # nn.Dropout(p=0.5),
            nn.Linear(128, 2)
        )


    def forward(self, x):
        out = self.cnn(x)
        out = out.view(out.size()[0], -1)

        return self.fc(out)
def main():
    net=Classifier()
    input=torch.randn(4,1,30,9)
    output=net.cnn(input)
    print(output.shape)

if __name__ == '__main__':
    main()