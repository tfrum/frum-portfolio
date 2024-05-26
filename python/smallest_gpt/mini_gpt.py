import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Define the structure of our neural network. This one is an FNN.
class GPT(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GPT, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Define our sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Create a new GPT model
model = GPT(10, 10, 10)

# Create an input matrix
input = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Convert the input to a tensor, I don't know how this works under the hood.
input = torch.tensor(input, dtype=torch.float32)

# Perform a single forward pass
output = model(input)

print(output)