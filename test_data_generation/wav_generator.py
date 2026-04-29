import os
import tempfile
import logging

from yapper import PiperSpeaker, PiperVoiceGermany

class WavGenerator:
    def __init__(self):
        self.speakers = [ PiperSpeaker(voice) for voice in PiperVoiceGermany ]

    def generate(self, move):
        result = []

        for text in move.full_texts():
            for speaker in self.speakers:
                tmp_fd, tmp_path = tempfile.mkstemp(suffix=".wav")
                os.close(tmp_fd)
                try:
                    speaker.text_to_wave(text, tmp_path)
                    with open(tmp_path, "rb") as f:
                        result.append(f.read())
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
        return result