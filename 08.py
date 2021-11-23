import torch
x = torch.tensor([3.0,5.0])
y = torch.tensor(2.0)
print(x*y)

x = torch.arange(12).reshape(3,4)
print(x)
print(x[2])
print(len(x))
print(x.shape)
print(x.T)

x = torch.arange(24).reshape(2,3,4)
print(x)

A = torch.arange(20,dtype=torch.float32).reshape(5,4)
B = A.clone()
print(A)
print(A+B)
print(A*B)


u = torch.tensor([3.0,4.0])
print(torch.norm(u))
print(torch.abs(u).sum())