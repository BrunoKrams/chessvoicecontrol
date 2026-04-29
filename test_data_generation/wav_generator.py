import os, logging

from yapper import PiperSpeaker, PiperVoiceGermany


class WavGenerator():
    logger = logging.getLogger("WavGenerator")

    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.speaker = [PiperSpeaker(voice) for voice in list(PiperVoiceGermany)]

    def generate(self, text: str, prefix: str):
        output_dir = os.path.join(self.base_dir, prefix)
        os.makedirs(output_dir, exist_ok=True)

        for i, speaker in enumerate(self.speaker):
            output_file = os.path.join(output_dir, f"{prefix}_{i}.wav")
            speaker.text_to_wave(text, output_file)
