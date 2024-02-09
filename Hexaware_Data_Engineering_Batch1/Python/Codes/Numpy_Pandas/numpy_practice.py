import numpy as np

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C=np.array(cvalues)
print(C)

print(C*9/5+32)
print(C)
print(type(C))

a=np.arange(1,10)
print(a)    

x=np.arange(10.4)
print(x)

x = np.arange(0.5, 10.4, 0.8)
print(x)

print(np.linspace(1,10))
print(np.linspace(1,10,7))
print(np.linspace(1,10,7,endpoint=False))

samples,spacing=np.linspace(1, 10, retstep=True)
print(spacing)

samples, spacing=np.linspace(1, 10, 20, endpoint=True, retstep=True)
print(spacing)

samples, spacing=np.linspace(1, 10, 20, endpoint=False, retstep=True)
print(spacing)

