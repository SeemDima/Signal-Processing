import matplotlib.pyplot as plt
import numpy as np
import cmath
import copy

def conv(func1, func2):
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

def convCutted(func1, func2):
    resultFuncListFull = conv(func1, func2)
    resultFuncList = []
    len1 = len(func1)
    len2 = len(func2)
    
    if len2 > len1:
        for i in range(len2):
            resultFuncList.append(resultFuncListFull[i])
    else:
        for i in range(len1):
            resultFuncList.append(resultFuncListFull[i])
    return resultFuncList

# https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80_%D0%91%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%B2%D0%BE%D1%80%D1%82%D0%B0
def ButterworthFilterW(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    filterListW = []
    k = 1j*(2*np.pi/paramSreza)
    for i in range(listSize):
        amp = pow(Amplitude,2) / (1 + pow(i/paramSreza,2*n))
        if i <= paramSreza:
            angle = (-i/paramSreza) * np.pi
        else:
            angle = 0        
        filterListW.append(amp*np.exp(1j * angle))
    return filterListW

def ButterworthFilter(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    filterListW = ButterworthFilterW(paramSreza, Amplitude, n, listSize)

    filterListT = np.fft.ifft(filterListW)

    filterListTcutted = []
    for i in range(int(listSize/2)):
        filterListTcutted.append(filterListT[i])
    for i in range(int(listSize/2)):
        filterListTcutted.append(0)
    return filterListTcutted


sSignal = 1000
sFilter = 1000

    
filterListW = ButterworthFilterW(int(sFilter/20), 2, 5, sFilter)
filterList = ButterworthFilter(int(sFilter/20), 4, 5, sFilter)

tFilter = np.linspace(0, int(sFilter/10), sFilter)
tSignal = np.linspace(0, int(sSignal/10), sSignal)
tConv = np.linspace(0, int(sSignal/10), sSignal + sFilter - 1)

signalList = 5*np.sin(  tSignal)
for i in range (sSignal):
    signalList[i] = signalList[i] + np.sin(300*i)#0.5*(np.random.random() - 0.5)

filteredSignalList = convCutted(signalList, filterList)
filteredSignalListFull = conv(signalList, filterList)


# PLOT
plt.figure('Filter characteristics')
plt.plot(tFilter, np.absolute(filterListW), 'g', label = u'abs обрезанного фильтра в W')
plt.plot(tFilter, np.angle(filterListW), 'y', label = u'angle обрезанного фильтра в W')
plt.plot(tFilter, np.abs(np.fft.fft(signalList, sSignal))/500, 'r', label = u'сигнал в W')
plt.legend()
plt.grid()

plt.figure('signal filtering')

plt.plot(tSignal, signalList, 'g', label = u'сигнал')
plt.plot(tSignal, np.real(filteredSignalList), 'r', label = u'фильтрованный сигнал')
plt.plot(tConv, np.real(filteredSignalListFull), 'y', label = u'результат свёртки' )

plt.legend()
plt.grid()
plt.show()

