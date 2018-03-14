import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

piX2 = 2.0 * cmath.pi # 2 Pi

def DFT(funcList):
    N = len(funcList)
    FuncList = []
    for k in range(N):
        fElem = np.imag(0)
        for n in range(N):
            arg = 1j * piX2 * k * n / N
            temp = funcList[n] * np.exp(- arg) # 1j == i(in real math)
            fElem = fElem + temp
        FuncList = np.append(FuncList, fElem)
    return FuncList
        
def InverseDFT(FuncList):
    N = len(FuncList)
    funcList = []
    for k in range(N):
        fElem = np.imag(0)
        for n in range(N):
            arg = 1j * piX2 * n * k / N
            temp = FuncList[n] * np.exp(arg)
            fElem = fElem + temp
        funcList.append(fElem / N)
    return funcList

N = 2000 # arrays size
halfN = 1000 # half of arrays size
t = np.linspace(-100*piX2, 100*piX2, N) # time line

func = [] # start function
for i in range (0, halfN):
    func.append(np.sin(t[i]))
for i in range (halfN, N):
    func.append(np.sin(t[i] + 3))
    
Ffunc = DFT(func) # FFT of start function
Bfunc = InverseDFT(Ffunc) # IFFT of fft result

deltaResultFunc = [] # delta between IFFT result and start function
for i in range (0, N):
    deltaResultFunc.append(Bfunc[i] - func[i])
    
fig, ax = plt.subplots()
fig2, delta = plt.subplots()

ax.plot(t, func)
ax.plot(t, abs(Ffunc), 'r')
#ax.plot(t, Bfunc, 'y')
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Фурье')
ax.grid()

delta.plot(t, np.angle(Ffunc))
delta.set(xlabel='time (s)', ylabel='phase', title='delta InverseDFT and real function')
delta.grid();


fig.savefig("test1.png")
fig2.savefig("deltaDFT.png")
plt.show()
