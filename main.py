import numpy as np
import pylab
from scipy.io.wavfile import write
from scipy.io import wavfile
import scipy.io.wavfile
import os
from soundcheck import Soundcheck
import wave
import matplotlib.pyplot as plt
f = Soundcheck()

# sampling rate
Fs = 44100.0  # Hz

# play length
tlen = 10  # s
Ts = 1 / Fs  # sampling interval
t = np.arange(0, tlen, Ts)  # time array

sin_freq = 22000# Hz
signal = np.sin(2 * np.pi * sin_freq * t)

sin_freq3 = 1400 #Hz
signal3 = np.sin(2*np.pi*sin_freq3*t)

sin_freq2 = 22000 # to make Hz people cannot hear
signal2 = np.sin(2*np.pi*sin_freq2*t)
# generate noise
signal_n = signal + 10000000*signal2 + 100*signal3

signal_f = np.fft.fft(signal_n)
freq = np.fft.fftfreq(len(t), Ts)

pylab.plot(freq, 20 * np.log10(np.abs(signal_f)))
pylab.xlim(0, Fs / 2)
pylab.show()

#makesignal_f = np.fft.fft(signal_n)
makefreq = [440, 880, 22000]

fs, data = scipy.io.wavfile.read('test10.wav')

signal_f = np.fft.fft(data)

freq = np.linspace(0, fs, len(20*np.log10(np.abs(signal_f))))

pylab.plot(freq, 20 * np.log10(np.abs(signal_f)))
pylab.xlim(0, Fs / 2)
pylab.show()

print(freq)
print(signal_f)

f.soundanalysis(freq, signal_f, makefreq)

print(f.cntvalue())
print(f.cheatcntvalue())



