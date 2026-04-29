import logging
import os
import re

from _pytest._py import path

import wav_generator
from json_generator import JsonGenerator
from model.moves import all_moves
from model.moves.move import Move
from wav_generator import WavGenerator


class DataGenerator():

    logger = logging.getLogger("DataGenerator")

    def __init__(self, target_dir: str):
        self.target_dir = target_dir

    def generate(self):
        os.makedirs(self.target_dir, exist_ok=True)
        for move in all_moves.all():
            self.logger.info(f"Generating files for move {move.identifier()}")
            move_dir = os.path.join(self.target_dir, move.identifier())
            os.makedirs(move_dir, exist_ok=False)
            JsonGenerator(move_dir).generate(move)
            wav_gen = WavGenerator(base_dir=move_dir)
            for i, text in enumerate(move.full_texts()):
                wav_gen.generate(text, re.sub('[^a-zA-Z0-9 \n\.]', '', text))

