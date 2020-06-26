import pyaudio
import wave
import os
from is_adjacent import is_adjacent
from soundcheck import Soundcheck



def find_mic_index():
    
    po = pyaudio.PyAudio()
    for index in range(po.get_device_count()):
        desc = po.get_device_info_by_index(index)
        #if desc["name"] == "record":
        print("DEVICE: %s  INDEX:  %s  RATE:  %s " % (desc["name"], index, int(desc["defaultSampleRate"])))

Hz_array = [2008, 2339, 4928, 5158]
Hz_db = [10, 100, 10000, 1]


def record():
    
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 256
    RECORD_SECONDS = 6
    WAVE_OUTPUT_FILENAME = "kang_cheating_O.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=1,
                        frames_per_buffer=CHUNK)

    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()


    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return WAVE_OUTPUT_FILENAME

#녹음 filename : 저장될 파일 이름
filename = record()

#filename.wav 파일 재생
os.system(filename)

#filename.wav 분석
f = Soundcheck()
is_adjacent(filename, Hz_array, f, Hz_db)

