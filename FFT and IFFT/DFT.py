import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

piX2 = 2.0 * cmath.pi # 2 Pi

def DFT(funcList):
    N = len(funcList)
    FuncList = []
    for k in range(N):
        FElem = np.imag(0)
        for n in range(N):
            arg = 1j * piX2 * k * n / N
            temp = funcList[n] * np.exp(- arg) # 1j == i(in real math)
            FElem = FElem + temp
        FuncList = np.append(FuncList, FElem)
    return FuncList
        
def InverseDFT(FuncList):
    N = len(FuncList)
    funcList = []
    for k in range(N):
        fElem = np.imag(0)
        for n in range(N):
            arg = 1j * piX2 * n * k / N
            temp = FuncList[n] * np.exp(arg) # 1j == i(in real math)
            fElem = fElem + temp
        #funcList = np.append(funcList, FElem / N)
        funcList.append(fElem / N)
    return funcList

t = np.linspace(-10*piX2, 10*piX2, 200)

#for i in range(len(z_bin)-1):

func = np.sin(t) + np.sin(2*t)

Ffunc = DFT(func)

Bfunc = InverseDFT(Ffunc)

standartFfunc = np.fft.fft(func)
standartBfunc = np.fft.ifft(standartFfunc)

# PLOT
fig, ax = plt.subplots()
fig2, delta = plt.subplots()

ax.plot(t, func)
ax.plot(t, Ffunc, 'r')
ax.plot(t, standartBfunc, 'g')
ax.plot(t, standartFfunc, 'y')
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Фурье')
ax.grid()

delta.plot(t, Ffunc - standartFfunc, 'r')
delta.plot(t, Bfunc - standartBfunc, 'g')
delta.plot(t, Bfunc - func, 'b', label = "deltaFunc")
delta.set(xlabel='time (s)', ylabel='voltage (mV)', title='delta')
delta.grid();


fig.savefig("test1.png")
fig2.savefig("deltaDFT.png")
plt.show()
