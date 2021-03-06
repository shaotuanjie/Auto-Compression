import numpy as np
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler
import os

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

def get_loaders(train_portion, batch_size, path_to_save_data, logger):
    traindir = os.path.join('/data/imagenet', 'train')

    train_transform = transforms.Compose([
            transforms.RandomResizedCrop(224, scale=(0.2, 1.0)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])

    train_loader = torch.utils.data.DataLoader(
            datasets.ImageFolder(traindir, train_transform),
            batch_size=batch_size, shuffle=True, num_workers=32, pin_memory=True)

    if train_portion == 1:
        return train_loader
    
    val_loader = torch.utils.data.DataLoader(
            datasets.ImageFolder(traindir, train_transform),
            batch_size=batch_size, shuffle=True, num_workers=16, pin_memory=True)
    
    return train_loader, val_loader
    
def get_test_loader(batch_size, path_to_save_data):
    valdir = os.path.join('/data/imagenet', 'val')
    
    val_transform = transforms.Compose([
            transforms.Resize(int(224/0.875)),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize,
            ])
    
    val_loader = torch.utils.data.DataLoader(
            datasets.ImageFolder(valdir, val_transform),
            batch_size=batch_size, shuffle=True, num_workers=32, pin_memory=True)

    return val_loader
