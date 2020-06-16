import numpy as np
import pylab
from scipy.io.wavfile import write
from scipy.io import wavfile
import scipy.io.wavfile
import os
from soundcheck import Soundcheck
import wave
import matplotlib.pyplot as plt

def is_adjacent(sound, makefreq, makedb, f) :
    
    fs, data = scipy.io.wavfile.read(sound)

    signal_f = np.fft.fft(data)

    freq = np.linspace(0, fs, len(20*np.log10(np.abs(signal_f))))

    f.soundanalysis(freq, signal_f, makefreq, makedb)

