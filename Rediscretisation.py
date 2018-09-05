import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal


def to_int(real1, real2):
    while (real1 - int(real1)) != 0 and (real2 - int(real2)) != 0:
        real1 *= 10
        real2 *= 10
    return int(real1), int(real2)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def lcm(a, b): # least common multiple
    return abs(a * b) // gcd(a, b) if a and b else 0


def interpolate(signal, time, expansion):
    signal_ = []
    time_ = []
    dt = (time[1] - time[0]) / expansion

    for i in range(len(signal) - 1):
        signal_.append(signal[i])
        signal_.extend([0] * (expansion - 1))

        time_.extend([time[i] + dt * j for j in range(expansion)])

    signal_.append(signal[-1])
    time_.append(time[-1])

    return signal_, time_


def decimate(signal, time, compression):
    signal_ = []
    time_ = []

    for i in range(0, len(signal), compression):
        signal_.append(signal[i])
        time_.append(time[i])

    return signal_, time_


def butter_lowpass(cutoff, fs, order=5):
    normal_cutoff = (cutoff / fs)*0.999999999
    b, a = scipy.signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = scipy.signal.filtfilt(b, a, data)
    return y


def resample(s, t, f1, f2):
    f1, f2 = to_int(f1, f2)
    m = lcm(f1, f2)
    order = 5
    si, ti = interpolate(s, t, m // f1)
    si = [i * (m // f1) for i in si]
    sf = butter_lowpass_filter(si, f1, m, order)
    sd, td = decimate(sf, ti, m // f2)

    return sd, td



kRedisc = 1.2

N1 = 500
N2 = kRedisc * N1;

periodNumber = 1

f1 = N1 / periodNumber
f2 = N2 / periodNumber

tSignal = np.linspace(-3*np.pi + periodNumber * 2 * np.pi, -np.pi + periodNumber * 2 * np.pi, N1)
signal = []
signalRedics = []
for i in range(N1):
    signal.append(np.sin(-np.pi + 2*np.pi * i / N1 + np.random.random_sample() - 1))


signalRedics, tSignalRedisc = resample(signal, tSignal, f1, f2)

plt.figure('Rediscretisation')
plt.subplot(311)
plt.title('signal')
plt.plot(tSignal, signal, 'bo', markersize = 2)
plt.plot(tSignal, signal, 'k', linewidth = 0.5)

plt.subplot(312)
plt.title('Rediscretisation of signal')
plt.plot(tSignalRedisc, signalRedics, 'ro', markersize = 1)
plt.plot(tSignalRedisc, signalRedics, 'k', linewidth = 0.5)

plt.subplot(313)
plt.title('signal & signalRedisc')

plt.plot(tSignal, signal, 'bo', markersize = 2)
plt.plot(tSignal, signal, 'k', linewidth = 0.5)

plt.plot(tSignalRedisc, signalRedics, 'rs', markersize = 2)
plt.plot(tSignalRedisc, signalRedics, 'r', linewidth = 0.5)
plt.show()
