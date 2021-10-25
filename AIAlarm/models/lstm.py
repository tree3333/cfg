from torch import nn
import torch
class lstm_reg(nn.Module):
    def __init__(self, input_size=20*9, hidden_size=8, output_size=2, num_layers=2):
        super(lstm_reg, self).__init__()

        self.rnn = nn.LSTM(input_size, hidden_size, num_layers)  # rnn
        self.reg = nn.Linear(hidden_size, output_size)  # 回归

    def forward(self, x):
        x, _ = self.rnn(x)  # (seq, batch, hidden)
        s, b, h = x.shape
        x = x.view(s * b, h)  # 转换成线性层的输入格式
        x = self.reg(x)
        return x
def main():
    data_=torch.randn((1,4,180))
    model = lstm_reg(20*9, 4)
    output = model(data_)
    #print(output)
if __name__ == '__main__':
    main()
