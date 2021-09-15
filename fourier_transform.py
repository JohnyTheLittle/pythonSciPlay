import matplotlib.pyplot as plt
import numpy as np
from numpy import fft


def signal(t, freq_1=4.0, freq_2=7.0):
    return np.sin(freq_1*2*np.pi*t)+np.sin(freq_2*2*np.pi*t)


t = np.linspace(0, 2, 100000)
y = signal(t)
y1 = signal(t, 0, 3.9)

fig, ax = plt.subplots()

#ax.plot(t, y)
print(f"y1{y1}")
print(t)
print(y)

state = np.random.RandomState(12345)
sample_size = 2**7
sample_t = np.linspace(0, 4, sample_size)
sample_y = signal(sample_t)+state.standard_normal(sample_size)
sample_d = 4./(sample_size - 1)
true_signal = signal(sample_t)
print(f"state={state}, sample_size={sample_size}, sample_t={sample_t}, sample_y={sample_y}")

ax.plot(sample_t, sample_y, "k.", label="Noisy signal")
ax.plot(sample_t, signal(sample_t), "k--", label="True signal")

spectrum = fft.fft(sample_y)
print("SPECTRUM", spectrum)
freq = fft.fftfreq(sample_size, sample_d)
pos_freq_i = np.arange(1, sample_size//2, dtype=int)


psd = np.abs(spectrum[pos_freq_i])**2+np.abs(spectrum[-pos_freq_i])**2

fig2, ax2 = plt.subplots()
ax2.plot(freq[pos_freq_i], psd)
plt.show()
