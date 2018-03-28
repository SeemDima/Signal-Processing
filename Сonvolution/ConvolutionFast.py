import matplotlib.pyplot as plt
import numpy as np
import copy
import random

def conv(func1, func2):
    func1List = copy.copy(func1)
    func2List = copy.copy(func2)
    
    resultFuncList = []
    len1 = len(func1List)
    len2 = len(func2List)
    N = len2 # N - наибольшая длина
    
    deltaLen = abs(len2 - len1)
    if len2 > len1:
        N = len2
        for t1 in range (deltaLen):
            func1List.append(0)
    elif len1 > len2:
        N = len1
        for t1 in range (deltaLen):
            func2List.append(0)
    
    # забиваем нули в начало сигнала чтобы свертка работала
    for t1 in range (N):
        func1List.insert(0,0)
    for t2 in range (N):
        func2List.insert(0,0)

    # свёртываем два сигнала в третий    
    for n in range(len1 + len2):
        resElem = 0
        for m in range (len1 + len2):
            resElem = resElem + func1List[m] * func2List[n - m]
        resultFuncList.append(resElem)
    return resultFuncList

def fastConv(func1, func2):
    func1List = copy.copy(func1)
    func2List = copy.copy(func2)
    
    len1 = len(func1List)
    len2 = len(func2List)
    N = len2 # N - наибольшая длина
    
    deltaLen = abs(len2 - len1)
    if len2 > len1:
        N = len2
        for t1 in range (deltaLen):
            func1List.append(0)
    elif len1 > len2:
        N = len1
        for t1 in range (deltaLen):
            func2List.append(0)
    
    # забиваем нули в начало сигнала чтобы свертка работала
    for t1 in range (N):
        func1List.insert(0,0)
    for t2 in range (N):
        func2List.insert(0,0)

    #фурье обоих сигналов
    dftFunc1 = np.fft.fft(func1List)
    dftFunc2 = np.fft.fft(func2List)

    resultDftFuncList = []
    for x in range(len1 + len2):
        resultDftFuncList.append(dftFunc1[x] * dftFunc2[x])

    return np.fft.ifft(resultDftFuncList)

        
N = 1000            # arrays size
halfN = int (N/2)   # half of arrays size
quaterN = int (N/4) # quater of arrays size

t = np.linspace(0, halfN, N) # time line
t2 = np.linspace(-halfN, halfN, 2*N) # time line2

func1 = []
func2 = []

for i in range (0, N):
    func1.append(random.random() - 0.5)
    func2.append(random.random() - 0.5)

convFunc1 = fastConv(func1, func2)
convFunc2 = conv(func1, func2)

# PLOT
plt.figure(1)
plt.plot(t, func1, 'r')
plt.plot(t, func2, 'g')
plt.figure(2)
plt.title('delta fast conv and common conv')
plt.plot(t2, convFunc1 - convFunc2)
plt.show()
