import numpy as np
import pylab
from scipy.io.wavfile import write
import os

class Soundcheck:
    cnt = 0
    cheatcnt = 0
    def __init__(self):
        self.cnt = 0
        self.cheatcnt = 0

    def soundanalysis(self, freq, signal_f, makefreq, makedb):
        flag = 0
        for i in range(len(freq)) :
            if (20*np.log10(np.abs(signal_f[i]))) >= 109 :
                for j in range(len(makefreq)) : 
                    if freq[i]  <= makefreq[j] * 1.00005 and freq[i] >= makefreq[j] * 0.99995 and (20*np.log10(np.abs(signal_f[i]))) <= makedb[j]* 1.2 and (20*np.log10(np.abs(signal_f[i]))) >= (20*np.log10(np.abs(signal_f[i]))) :
                        flag = 1
                        print(freq[i])
                    else :
                        if flag == 1 :
                            flag = 0
                            self.cnt+=1
                            break
        if len(makefreq) == self.cnt :
            self.cheatcnt+=1 
    
    def cntzero(self):
        self.cnt = 0
    def cntvalue(self):
        return self.cnt
    def cheatcntvalue(self):
        return self.cheatcnt
    

