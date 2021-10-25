import warnings
import torch
class DefaultConfig(object):

    #测试集的路径
    原始的测试数据路径='./原始data____true.csv'
    处理后的测试数据路径='./处理后合并数据.csv'

    env = 'default132'  # visdom 环境
    vis_port = 8097  # visdom 端口
    model = 'Classifier'  # 使用的模型，名字必须与models/__init__.py中的名字一致
    prefix='checkpoints/modelCNN_0_'
    result_file='./测试结果/测试结果.csv'

    # 训练数据
    train_data_root0_原始 ='./原始data____False.csv'# 训练集存放路径
    train_data_root1_原始 = './原始data____true.csv'

    train_data_root0_处理后='./处理后data___False__长度30.csv'
    train_data_root１_处理后 = './处理后data___True__长度30.csv'

    test_data_root0 = 'test_False.csv'  # 测试集存放路径
    test_data_root1 = 'test_true.csv'


    load_model_path = 'checkpoints/_modelmax.pth'  # 加载预训练的模型的路径，为None代表不加载
    # load_model_path=None

    batch_size = 32  # batch size
    use_gpu = False  # user GPU or not
    num_workers = 4  # how many workers for loading data
    print_freq = 20  # print info every N batch
    max_epoch = 200
    lr = 1e-3  # initial learning rate
    lr_decay = 0.5  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 1e-5  # 损失函数
    device = torch.device('cuda')

    def _parse(self, kwargs):
        """
        根据字典kwargs 更新 config参数

        """
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribut %s" % k)
            setattr(self, k, v)
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('_'):
                print(k, getattr(self, k))

opt = DefaultConfig()
