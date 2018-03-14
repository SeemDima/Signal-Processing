import matplotlib.pyplot as plt
import numpy as np

piX2 = 2.0 * np.pi # 2 Pi

def Conv(func1List, func2List):
    resultFuncList = []
    len1 = len(func1List)
    len2 = len(func2List)
    if (len1 != len2)
        return resultFuncList
    for x in range(len1):
        fElem = np.imag(0)
        for y in range(len2):
            arg = 1j * piX2 * k * n / N
            temp = funcList[n] * np.exp(- arg) # 1j == i(in real math)
            fElem = fElem + temp
        FuncList = np.append(FuncList, fElem)
    return resultFuncList
        

N = 2000 # arrays size
halfN = 1000 # half of arrays size
t = np.linspace(-100*piX2, 100*piX2, N) # time line

func = [] # start function
for i in range (0, N):
    func.append(0)
for i in range (N, N + halfN):
    func.append(1)
for i in range (N + halfN, N + N):
    func.append(0)

# PLOT
fig, ax = plt.subplots()
ax.plot(t, func)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Convolution')
ax.grid()
plt.show()
