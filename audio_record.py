import pyaudio
import wave
import os


def find_mic_index():
    po = pyaudio.PyAudio()
    for index in range(po.get_device_count()):
        desc = po.get_device_info_by_index(index)
        #if desc["name"] == "record":
        print("DEVICE: %s  INDEX:  %s  RATE:  %s " %  (desc["name"], index,  int(desc["defaultSampleRate"])))

def record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 11
    WAVE_OUTPUT_FILENAME = "record1.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=1,
                        frames_per_buffer=CHUNK)
    # print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("finished recording")

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

record()
os.system("start record1.wav")

