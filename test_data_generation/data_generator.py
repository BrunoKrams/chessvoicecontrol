import logging
import os

from .json_generator import JsonGenerator
from .wav_generator import WavGenerator

class DataGenerator():

    def __init__(self, target_dir: str):
        self.target_dir = target_dir

    def generate(self, move):
        identifier =  move.identifier()
        os.makedirs(self.target_dir, exist_ok=True)
        move_dir = os.path.join(self.target_dir, identifier)
        os.makedirs(move_dir, exist_ok=False)
        JsonGenerator(move_dir).generate(move)
        wav_gen = WavGenerator(base_dir=move_dir)
        for i, text in enumerate(move.full_texts()):
            wav_gen.generate(text, f"text_{i}")


