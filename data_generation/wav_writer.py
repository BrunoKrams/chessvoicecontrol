from yapper import PiperSpeaker

class WavWriter():
    def __init__(self, piper_speaker: PiperSpeaker):
        self.piper_speaker = piper_speaker

    def generate_wav(self, text:str, file_name:str):
        self.piper_speaker.text_to_wave(text, file_name)
