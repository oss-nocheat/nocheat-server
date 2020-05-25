import numpy as np
import pylab
from scipy.io.wavfile import write
import os

# sampling rate
Fs = 44100.0  # Hz

# play length
tlen = 10  # s
Ts = 1 / Fs  # sampling interval
t = np.arange(0, tlen, Ts)  # time array

student_cnt = 50 # number of student(connect to client's)

# generate signal
sin_freq = 440  # Hz
sin_freq3 = 880 #Hz
signal = np.sin(2 * np.pi * sin_freq * t)
signal3 = np.sin(2*np.pi*sin_freq3*t)

sin_freq2 = 22000 # to make Hz people cannot hear
signal2 = np.sin(2*np.pi*sin_freq2*t)

# generate noise
#noise = np.random.uniform(-1, 1, len(t)) * 0.1
#print(noise)

# signal + noise
signal_n = signal + 10000000*signal2 + 1000*signal3 #+ noise
print(signal_n)

# fft
signal_f = np.fft.fft(signal_n)
freq = np.fft.fftfreq(len(t), Ts)
print(signal_f)

# plot
pylab.plot(freq, np.log10(np.abs(signal_f)))
pylab.xlim(0, Fs / 2)
pylab.show()

# save as wav file
scaled = np.int16(signal_n / np.max(np.abs(signal_n)) * 32767)
write('test.wav', 44100, scaled)

# play wav file
os.system("start test.wav")