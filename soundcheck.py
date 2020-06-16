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

    def soundanalyzer(self, freq, signal_f, makefreq, makedb):
        flag = 0
        dbsum = 0
        datacnt = 0
        dbmeanarray = []
        for i in range(len(freq)) :
            if (20*np.log10(np.abs(signal_f[i]))) >= 109 :
                for j in range(len(makefreq)) : 
                        flag = 1
                    if freq[i]  <= makefreq[j] * 1.00005 and freq[i] >= makefreq[j] * 0.99995  :
                        dbsum = dbsum + 20*np.log10(np.abs(signal_f[i]))
                        datacnt = datacnt + 1
                    else :
                        print(freq[i])
                        if flag == 1 :
                            self.cnt+=1   
                            flag = 0
                            dbmeanarray.append(dbsum/datacnt)
                            datacnt = 0
                            dbsum = 0
                            break
        if len(makefreq) == self.cnt :
            flagt = 0
            for i in range(len(makefreq)) :
                for j in range(i+1 ,len(makefreq)) :
                    if makefreq[i] <= makefreq[j] and dbmeanarray[i] <= dbmeanarray[j] :
                        continue
                    elif makefreq[i] >= makefreq[j] and dbmeanarray[i] >=dbmeanarray[j] :
                        continue
                        flagt = 1
                    else :
                        break
                if flagt == 1 :
                    break
            if flagt == 0 :
                self.cheatcnt+=1 
    
    def cntzero(self):
        self.cnt = 0
    def cntvalue(self):
        return self.cnt
    def cheatcntvalue(self):
        return self.cheatcnt
    

