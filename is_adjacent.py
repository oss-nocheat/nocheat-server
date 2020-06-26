import numpy as np
import pylab
from scipy.io.wavfile import write
from scipy.io import wavfile
import scipy.io.wavfile
import os
from soundcheck import Soundcheck
import wave
import matplotlib.pyplot as plt


def is_adjacent(sound, makefreq, f, makedb):
    
    fs, data = scipy.io.wavfile.read(sound)

    # print(fs, data)
    signal_f = np.fft.fft(data)
    # print(signal_f)

    freq = np.linspace(0, fs, len(20 * np.log10(np.abs(signal_f))))

    Fs = 44100.0
    pylab.plot(freq, 20 * np.log10(np.abs(signal_f)))
    pylab.xlim(0, Fs / 2)
    pylab.show()

    f.soundanalysis(freq, signal_f, makefreq, makedb)

    print(sound, end=' : ')
    if f.cheatcntvalue() == 1:
        print("Detect cheating")
    else:
        if f.cntvalue() == 4:
            print("Doubt cheating")
        else:
            print("Innocence")
