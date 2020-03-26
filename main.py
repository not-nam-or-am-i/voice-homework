import keyboard
import function
import sounddevice as sd
import soundfile as sf
import time

count = 0
is_recording = False
FILE_NAME = 'data'
FILE_TYPE = '.wav'
SR = 22050
DURATION = 15
CHANNEL = 1
data = []

print(sd.default.device)

while True:
    if keyboard.is_pressed('space') and is_recording is False:
        is_recording = True
        data = function.record(DURATION, SR, CHANNEL)
    if keyboard.is_pressed('space') and is_recording is True:
        sd.stop()
        sf.write(FILE_NAME + str(count) + FILE_TYPE, data=data, samplerate=SR)
        count = count + 1
        time.sleep(0.25)
        print('done recording')
        is_recording = False
    if keyboard.is_pressed('esc'):
        break
