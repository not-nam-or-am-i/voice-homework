import sys
from venv import logger

import keyboard
import soundfile as sf
import sounddevice as sd


def record(self):
    try:
        with sf.SoundFile(self.filepath,
                          mode='x', samplerate=self.SAMPLE_RATE,
                          channels=self.CHANNELS, subtype=None) as file:
            with sd.InputStream(samplerate=self.SAMPLE_RATE, device=self.mic_id,
                                channels=self.CHANNELS, callback=self.callback):
                logger.info(f"New recording started: {self.sound_file.name}")
                try:
                    while True:
                        file.write(self.mic_queue.get())
                except RuntimeError as re:
                    logger.debug(f"{re}. If recording was stopped by the user, then this can be ignored")
    except Exception:
        print(Exception)


def callback(self, indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    self.mic_queue.put(indata.copy())

def stop_mic_recording(self):
    try:
        self.sound_file.flush()
        self.sound_file.close()
        logger.info(f"Stopped and closed recording: {self.sound_file.name}")

    except RuntimeError as e:
        logger.info(f"Error stopping/saving {self.sound_file.name}. Make sure the file exists and can be modified")
        logger.info(f"RunTimeError: \n{e}")


while True:
    if keyboard.is_pressed("space"):
        record()
    if keyboard.is_pressed('s'):
        stop_mic_recording()
    if