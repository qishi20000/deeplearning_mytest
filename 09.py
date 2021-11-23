import torch
a = torch.ones((2,5,4))
print(a.shape)
print(a.sum().shape)

print(a)
print(a.sum(axis=0))