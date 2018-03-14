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
    funcList = np.array
    for k in range(N):
        fElem = np.imag(0)
        for n in range(N):
            fElem = fElem + FuncList[n] * cmath.exp(1j * piX2 * k * n / N)
            np.append(funcList, fElem / N)
    return funcList

t = np.linspace(-10*piX2, 10*piX2, 2000)

#for i in range(len(t)-1):
    
func = np.sin(t) + np.sin(1.08*t)

Ffunc = DFT(func)

# PLOT
fig, ax = plt.subplots()
fig1, axPhase = plt.subplots()
ax.plot(t, func)
ax.plot(t, abs(Ffunc), 'r')
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Фурье')
ax.grid()

axPhase.plot(t, np.angle(Ffunc)) 
axPhase.set(xlabel='time (s)', ylabel='Phase', title='Фурье')
axPhase.grid()


fig.savefig("test1.png")
plt.show()
