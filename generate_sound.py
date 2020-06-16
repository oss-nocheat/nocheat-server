import numpy as np
import hashlib
import os
import pylab
from scipy.io.wavfile import write

def pprint(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

def makeSound(key):
    # sound_count: 소리의 개수! int형
    # sound_size: 소리의 크기 비율! list형
    # sound_hz: 소리의 주파수! list형
    # result: 위 세개를 순서대로 넣은 output 값
    # makeSound 함수: 1개의 output 소리를 만들때 필요한 정보를 생성함
    #                input-key(string): 해시 암호화의 키값으로 쓰일 값
    #                output- result(list): 2차원 리스트. list[0]: 소리의 개수(int), list[1]:소리의 크기비율(list), list[2]: 소리의 주파수(list)

    sound_size_ratio = []
    sound_hz = []
    result = []

    where = 8
    num = 0

    # hashr-sha256 hash 변환 결과
    hashr = hashlib.sha256(key.encode())
    hashr = hashr.hexdigest()
    hashr = int(hashr, 16)
    hashr = [int(i) for i in str(hashr)]

    sound_count = hashr[1] % 3 + 2

    for i in range(0, sound_count):
        sound_size_ratio.append(1)

    for i in range(0, 7):
        which = hashr[i + 1] % 3
        sound_size_ratio[which] = sound_size_ratio[which] + 1

    for i in range(0, sound_count):
        for j in range(0, 5):
            num = num + hashr[where + j] * (10 ** j)
        num = num % 15000
        where = where + 5
        hz = 5000 + num
        sound_hz.append(hz)
    result.append(sound_count)
    result.append(sound_size_ratio)
    result.append(sound_hz)

    print(result)
    return result


def generate_sound():
    list = makeSound("fege")

    # sampling rate
    Fs = 44100.0  # Hz
    # play length
    tlen = 5  # s
    Ts = 1 / Fs  # sampling interval
    t = np.arange(0, tlen, Ts)  # time array
    temp = []
    arr = [[0] * list[0] for _ in range(300000)]

    #a = np.sin(2 * np.pi * list[2][0] * t)
    #pprint(a)

    # to make sinwaves
    i = 0
    for i in range(0, list[0]):
        arr[i] = np.sin(2 * np.pi * list[2][i] * t)
        i = i+1

    # to combine sinwaves
    signal = 0
    i = 0
    for i in range(0, list[0]):
        signal = signal + 1000*list[1][i] * arr[i]

    # fft
    signal_fft = np.fft.fft(signal)
    signal_freq = np.fft.fftfreq(len(t), Ts)
    # print(signal_fft)

    # plot
    pylab.plot(signal_freq, np.log10(np.abs(signal_fft)))
    pylab.xlim(0, Fs / 2)
    pylab.show()

    # save as wav file
    scaled = np.int16(signal / np.max(np.abs(signal)) * 32767)
    write('signal.wav', 44100, scaled)

    return list

    # play wav file
    # os.system("start signal.wav")

#generate_sound()




