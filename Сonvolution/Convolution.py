import matplotlib.pyplot as plt
import numpy as np
import copy
import random

piX2 = 2.0 * np.pi # 2 Pi

def conv(func1, func2):
    func1List = copy.copy(func1)
    func2List = copy.copy(func2)
    
    resultFuncList = []
    len1 = len(func1List)
    len2 = len(func2List)

    deltaLen = abs(len2 - len1)
    if len2 > len1:
        for t1 in range (deltaLen):
            func1List.insert(0,0)
    elif len1 > len2:
        for t1 in range (deltaLen):
            func2List.insert(0,0)
    
    # забиваем нули в начало сигнала чтобы свертка работала
    for t1 in range (len2):
        func1List.insert(0,0)
    for t2 in range (len1):
        func2List.insert(0,0)

    # свёртываем два сигнала в третий    
    for n in range(len1 + len2):
        resElem = 0
        for m in range (len1 + len2):
            #print(func1List[m], func2List[n - m])
            
            elem = func1List[m] * func2List[n - m]
            
            resElem = resElem + elem
        resultFuncList.append(resElem)
    return resultFuncList

        
N = 1000            # arrays size
halfN = int (N/2)   # half of arrays size
quaterN = int (N/4) # quater of arrays size

t = np.linspace(0, halfN, N) # time line
t2 = np.linspace(-halfN, halfN, 2*N) # time line2

func1 = []
func2 = []
#for i in range (0, quaterN):
#    func1.append(0)
#    func2.append(0)
#for i in range (quaterN, quaterN + halfN):
#    func1.append(1)
#    func2.append(1)
#for i in range (quaterN + halfN, N):
#    func1.append(0)
#    func2.append(0)

for i in range (0, N):
    func1.append(random.random() - 0.5)
    func2.append(random.random() - 0.5)

convFunc = conv(func1, func2)


# PLOT
plt.figure(1)
plt.plot(t, func1, 'r')
plt.plot(t, func2, 'g')
plt.figure(2)
plt.plot(t2, convFunc)
plt.show()
