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

# HIGHT FREQUENCE FILTER BASED ON BUTTERWIRTHFILTER
def HFButterworthFilterW(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    filterListW = []
    k = 1j*(2*np.pi/paramSreza)
    for i in range(int(listSize/2)):
        amp = pow(Amplitude,2) - pow(Amplitude,2) / (1 + pow(i/paramSreza,2*n))
        angle = (-i/paramSreza) * np.pi
        filterListW.append(amp*np.exp(1j * angle))
    for i in range(int(listSize/2)):
        filterListW.append(filterListW[int(listSize/2) - 1 - i])
    return filterListW

def HFButterworthFilter(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    HFfilterListW = HFButterworthFilterW(paramSreza, Amplitude, n, listSize)

    

    filterListT = np.fft.ifft(HFfilterListW)

    filterListTcutted = []
    for i in range(int(listSize/2)):
        filterListTcutted.append(filterListT[i])
    for i in range(int(listSize/2)):
        filterListTcutted.append(0)
    return filterListTcutted
def ButterworthFilterW(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    filterListW = []
    k = 1j*(2*np.pi/paramSreza)
    for i in range(int(listSize/2)):
        amp = pow(Amplitude,2) / (1 + pow(i/paramSreza,2*n))
        if i <= paramSreza:
            angle = (-i/paramSreza) * np.pi
        else:
            angle = 0        
        filterListW.append(amp*np.exp(1j * angle))
    for i in range(int(listSize/2)):
        filterListW.append(filterListW[int(listSize/2) - i])
    return filterListW

def ButterworthFilter(paramSreza, Amplitude, n, listSize):
    timeSrez = listSize / paramSreza    
    filterListW = ButterworthFilterW(paramSreza, Amplitude, n, listSize)

    filterListT = np.fft.ifft(filterListW)

    filterListTcutted = []
    for i in range(int(listSize/10)):
        filterListTcutted.append(filterListT[i])
    for i in range(int(9*listSize/10)):
        filterListTcutted.append(0)
    return filterListTcutted


sSignal = 1000
sFilter = 1000

    
filterListW = HFButterworthFilterW(int(sFilter/6), 1.3, 5, sFilter)
filterList = HFButterworthFilter(int(sFilter/6), 1.3, 5, sFilter)

tFilter = np.linspace(0, int(sFilter/10), sFilter)
tSignal = np.linspace(0, int(sSignal/10), sSignal)
tConv = np.linspace(0, int(sSignal/10), sSignal + sFilter - 1)

signalList = 5*np.sin(  tSignal)
randList = []
for i in range (sSignal):
    randList.append(0.5*(np.random.random() - 0.5))#np.sin(300*i)
    signalList[i] = signalList[i] + randList[i]

filteredSignalList = convCutted(signalList, filterList)
filteredSignalListFull = conv(signalList, filterList)

filteredSignalListEasy = []
for i in range(sSignal):
    filteredSignalListEasy.append(signalList[i] - filteredSignalList[i])

filterListWres = np.fft.ifft(filterList)


# PLOT
plt.figure('Filter characteristics')
plt.plot(tFilter, np.absolute(filterListW), label = u'abs обрезанного фильтра в W')
plt.plot(tFilter, np.angle(filterListW), label = u'angle обрезанного фильтра в W')
plt.plot(tFilter, np.abs(np.fft.fft(signalList, sSignal))/500, 'r', label = u'сигнал в W')
plt.plot(tFilter, np.real(filterList), label = u'обрезанный фильтр в T')
plt.plot(tFilter, np.abs(filterListWres), label = u'обрезанный фильтр в W')

plt.legend()
plt.grid()

plt.figure('signal filtering')

plt.plot(tSignal, signalList, 'g', label = u'сигнал')
plt.plot(tSignal, randList, 'b', label = u'добавка к сигналу')
plt.plot(tSignal, np.real(filteredSignalList), 'r', label = u'фильтрованный сигнал')
#plt.plot(tSignal, np.real(filteredSignalListEasy), 'y', label = u'фильтрованный сигнал верхних частот' )

plt.legend()
plt.grid()
plt.show()

