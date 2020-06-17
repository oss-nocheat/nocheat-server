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
        flag = -1
        dbsum = 0
        datacnt = 0
        dbmeanarray = []
        for i in range(len(freq)):
            if (20 * np.log10(np.abs(signal_f[i]))) >= 90:
                for j in range(self.cnt, len(makefreq)):

                    # print(freq[i], makefreq[j], flag, self.cnt, (20*np.log10(np.abs(signal_f[i]))))
                    if freq[i] <= makefreq[j] * 1.0005 and freq[i] >= makefreq[j] * 0.9995:
                        flag = j
                        dbsum = dbsum + 20 * np.log10(np.abs(signal_f[i]))
                        datacnt = datacnt + 1
                        # print(freq[i], makefreq[j])
                        # os.system("Pause")
                    else:
                        if flag != -1:
                            self.cnt += 1
                            if datacnt != 0:
                                dbmeanarray.append(dbsum / datacnt)
                            flag = -1
                            datacnt = 0
                            dbsum = 0
                            # os.system("Pause")

        if len(makefreq) == self.cnt:
            flagt = 0
            for i in range(len(makefreq)):
                for j in range(i + 1, len(makefreq)):
                    # print(i, makedb[i], dbmeanarray[i], j, makedb[j], dbmeanarray[j])
                    if makedb[i] <= makedb[j] and dbmeanarray[i] <= dbmeanarray[j]:
                        continue
                    elif makedb[i] >= makedb[j] and dbmeanarray[i] >= dbmeanarray[j]:
                        continue
                    else:
                        flagt = 1
                        break
                if flagt == 1:
                    break
            if flagt == 0:
                self.cheatcnt += 1

    def cntzero(self):
        self.cnt = 0

    def cntvalue(self):
        return self.cnt

    def cheatcntvalue(self):
        return self.cheatcnt