import matplotlib.pyplot as plt
import numpy as np
import cmath
import copy

def convCutted(func1, func2):
    func1List = copy.copy(func1)
    func2List = copy.copy(func2)
    
    resultFuncList = []
    len1 = len(func1List)
    len2 = len(func2List)
    
    # свёртываем два сигнала в третий    
    for n in range (len1 + len2 - 1):
        resElem = 0
        for m in range (len1 + len2 - 1):
            if (n - m < len2) and (m < len1):
                resElem = resElem + func1List[m] * func2List[n - m]
        resultFuncList.append(resElem)
    return resultFuncList

sSignal = 1000

tSignal = np.linspace(0, int(sSignal/10), sSignal)
signalList = 5*np.sin(tSignal)

tConv = np.linspace(0, int(sSignal/10), sSignal + sSignal - 1)

convList = convCutted(signalList, signalList)

plt.figure('Conv test')
plt.plot(tSignal, signalList, 'r', label = u'сигнал')
plt.plot(tConv, convList, 'g', label = u'conv')
plt.grid()
plt.show()
