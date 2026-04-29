import os, logging

from yapper import PiperSpeaker, PiperVoiceGermany


class WavGenerator():
    def __init__(self):
        self.speaker = [PiperSpeaker(voice) for voice in list(PiperVoiceGermany)]

    def generate(self, move):
        result = []
        for text in move.full_texts():
            for speaker in enumerate(self.speaker):
                result.append[generate_wav_blob(text)]
                try:
                    speaker.text_to_wave(text, tmp_path)
                with open(tmp_path, "rb") as f:
                    result.append(f.read())
                finally:
                    os.remove(tmp_path)
        return result
