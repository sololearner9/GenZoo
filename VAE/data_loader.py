import torch
import torch.utils.data
from torchvision import datasets, transforms


def load_mnist(batch_size):
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('/data', train=True, download=True,
                       transform=transforms.ToTensor()),
        batch_size=batch_size, shuffle=True)

    return train_loader


