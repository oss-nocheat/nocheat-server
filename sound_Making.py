import numpy as np
import pylab
from scipy.io.wavfile import write
import os
import sound_analysis

# sampling rate
Fs = 44100.0  # Hz

# play length
tlen = 5  # s
Ts = 1 / Fs  # sampling interval
t = np.arange(0, tlen, Ts)  # time array



# generate signal
sin_freq = 8800  # Hz
sin_freq2 = 10000 #Hz
sin_freq_max = 22000 # to make Hz people cannot hear

signal = np.sin(2 * np.pi * sin_freq * t)
signal2 = np.sin(2*np.pi*sin_freq2*t)
signal_max = np.sin(2*np.pi*sin_freq_max*t)

signal_n = 10000*signal + 10000*signal2 + 10000000*signal_max

# fft
signal_fft = np.fft.fft(signal_n)
signal_freq = np.fft.fftfreq(len(t), Ts)
print(signal_fft)

# plot
pylab.plot(signal_freq, np.log10(np.abs(signal_fft)))
pylab.xlim(0, Fs / 2)
pylab.show()

# save as wav file
scaled = np.int16(signal_n / np.max(np.abs(signal_n)) * 32767)
write('signal.wav', 44100, scaled)

# play wav file
os.system("start test.wav")