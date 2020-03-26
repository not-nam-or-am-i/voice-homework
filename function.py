import sounddevice as sd


# record your voice to a new file
def record(duration, sr, channel):
    print('recording')
    my_rec = sd.rec(samplerate=sr, channels=channel, frames=int(sr * duration))
    return my_rec
