import torch
import torch.nn as nn


class NeuralCode(nn.Module):
    def __init__(self, input_size, hidden_size, number_classes):
        super(NeuralCode, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, number_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
       # no activation & no softmax
        return out
