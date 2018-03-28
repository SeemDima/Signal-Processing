import matplotlib.pyplot as plt
import numpy as np
import copy
import random

piX2 = 2.0 * np.pi # 2 Pi

def correlation(func1, func2):
    func1List = copy.copy(func1)
    func2List = copy.copy(func2)
    
    len1 = len(func1List)
    len2 = len(func2List)
    N = len2 # N - наибольшая длина

    # выравниваем размеры списков (меньший забиваем нулями в конец)
    deltaLen = abs(len2 - len1)
    if len2 > len1:
        N = len2
        for t1 in range (deltaLen):
            func1List.append(0)
    elif len1 > len2:
        N = len1
        for t1 in range (deltaLen):
            func2List.append(0)
            
    resultFuncList = []
    for j in range(-N, 0):
        elem = 0
        for n in range(N + j):
            elem = elem + (func1List[n] * func2List[n - j])
        resultFuncList.append(elem / N)
    for j in range(0, N):
        elem = 0
        for n in range(N - j):
            elem = elem + (func1List[n] * func2List[n + j])
        resultFuncList.append(elem / N)
    return resultFuncList
        
N = 1000            # arrays size
halfN = int (N/2)   # half of arrays size
quaterN = int (N/4) # quater of arrays size

t = np.linspace(0, halfN, N) # time line
t2 = np.linspace(-halfN, halfN, 2*N) # time line2

func1 = []
func2 = []

for i in range (0, N):
    func1.append(2*(random.random() - 0.5))
    func2.append(2*(random.random() - 0.5))

correlat = correlation(func1, func2)

# PLOT
plt.figure(1)
plt.plot(t, func1, 'r')
plt.plot(t, func2, 'g')
plt.figure(2)
plt.title('Correlation')
plt.plot(t2, correlat)
plt.show()
