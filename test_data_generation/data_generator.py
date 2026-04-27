import os

from yapper import PiperSpeaker, PiperVoiceGermany

from model.moves import all_moves
from wav_writer import WavWriter


class DataGenerator():

    def __init__(self, target_dir:str):
        self.target_dir = target_dir


    def run(self):
        index = 0
        moves = all_moves.all()
        os.makedirs(self.target_dir, exist_ok=True)
        for voice in list(PiperVoiceGermany):
            wav_writer = WavWriter(PiperSpeaker(voice))
            for move in moves:
                for text in move.full_texts():
                    index += 1
                    if index % 100 == 0:
                        print(f"Writing {index}")
                    wav_writer.generate_wav(text, os.path.join(self.target_dir, f"{index}.wav"))
