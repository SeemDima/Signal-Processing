import numpy as np

from scipy import signal
import matplotlib.pyplot as plt

def morletWT(M, w=5.0, s=1.0, complete=True):

    x = np.linspace(-s * 2 * np.pi, s * 2 * np.pi, M)
    output = np.real(np.exp(1j * w * x))

    if complete:
        output -= np.real(np.exp(-0.5 * (w**2)))

    output *= np.real(np.exp(-0.5 * (x**2)) * np.pi**(-0.25))

    return output


t = np.linspace(-2, 2, 500, endpoint=False)
sig = []
for i in range(100):
    sig.append(0)
for i in range(100):
    sig.append(1)
for i in range(100):
    sig.append(0)
for i in range(100):
    sig.append(1)
for i in range(100):
    sig.append(0)
#sig = np.sin(2 * np.pi * 7 * t)# + signal.gausspulse(t - 0.4, fc=2)
plt.figure("signal")
plt.plot(t, sig)

widths = np.arange(1, 51)

cwtmatr1 = signal.cwt(sig, signal.ricker, widths)
cwtmatr2 = signal.cwt(sig, morletWT, widths)
plt.figure("wavelet1")
plt.imshow(cwtmatr1, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
vmax=abs(cwtmatr1).max(), vmin=-abs(cwtmatr1).max())
plt.figure("wavelet2")
plt.imshow(cwtmatr2, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
vmax=abs(cwtmatr2).max(), vmin=-abs(cwtmatr2).max())
plt.show()
