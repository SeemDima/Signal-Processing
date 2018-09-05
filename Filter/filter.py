import matplotlib.pyplot as plt
import numpy as np
import cmath
piX2 = 2.0 * np.pi # 2 Pi

def Filter(funcList, P):
    FilteredFuncList = []
    length = len(funcList)
    
    for n in range(length):
        Elem = 0
        for i in range (-P, P + 1):
            if (n - i) < 0 or (n - i) >= N:
                continue
            Elem = Elem + (1/(2*P+1))*funcList[n - i]
        FilteredFuncList.append(Elem)
    return FilteredFuncList
        

func = []

N = 1000            # arrays size
halfN = int (N/2)   # half of arrays size
quaterN = int (N/4) # quater of arrays size
P = 100
t = np.linspace(0, N, N)
for i in range (0, quaterN):
    func.append(0)
for i in range (quaterN, quaterN + halfN):
    func.append(1)
for i in range (quaterN + halfN, N):
    func.append(0)

FiltFunc = Filter(func, P);

#momentum characteristic
filterCharact = []
DFTfilterCharact = []
for i in range (P):
    filterCharact.append(1/P + 1)
for i in range (N - P):
    filterCharact.append(0)
DFTfilterCharact = np.fft.fft(filterCharact)
# PLOT

plt.title('Фильтр скользящего среднего')
plt.plot(t, func)
plt.plot(t, FiltFunc)
plt.figure(2)
plt.title('импульсная характеристика')
plt.plot(t, abs(DFTfilterCharact))
plt.plot(t, np.angle(DFTfilterCharact), 'r')
plt.grid()

plt.show()

