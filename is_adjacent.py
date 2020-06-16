    freq = np.linspace(0, fs, len(20*np.log10(np.abs(signal_f))))
import os
from soundcheck import Soundcheck
import wave
import matplotlib.pyplot as plt
def check_adjacent(sound, makefreq, makedb, f) :

    
    fs, data = scipy.io.wavfile.read(sound)

    signal_f = np.fft.fft(data)


    f.soundanalyzer(freq, signal_f, makefreq, makedb)

