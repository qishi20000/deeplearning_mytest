import torch
x = torch.arange(4.0,requires_grad=True)
print(x.grad)

y = 2*torch.dot(x,x)
y.backward()
print(x.grad)