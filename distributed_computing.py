import os
from pathlib import Path

import ray

from test_data_generation.json_generator import JsonGenerator
from test_data_generation.model.moves import all_moves
from test_data_generation.wav_generator import WavGenerator


@ray.remote
class MoveCollector:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def write_move(self, move_id, json, wavs):
        move_dir = os.path.join(self.data_dir, move_id)
        os.makedirs(move_dir, exist_ok=True)

        with open(os.path.join(move_dir, "move.json"), "w") as f:
            f.write(json["move"])

        with open(os.path.join(move_dir, "mask.json"), "w") as f:
            f.write(json["mask"])

        for i, wav in enumerate(wavs):
            path = os.path.join(move_dir, f"wav_{i:03d}.wav")
            with open(path, "wb") as f:
                f.write(wav)

        return {
            "move_id": move_id,
            "num_wavs": len(wavs),
            "path": move_dir,
        }

@ray.remote(num_cpus=1)
def process_move(move, collector):
    json_gen = JsonGenerator()
    jsons = json_gen.generate(move)
    wav_gen = WavGenerator()
    wavs = wav_gen.generate(move)
    return collector.write_move.remote(
        move.identifier(),
        jsons,
        wavs
    )

def main():
    working_dir = str(Path(__file__).resolve().parent)
    ray.init(address="auto", runtime_env={"working_dir": working_dir})
    moves = all_moves.all()[1:3]
    collector = MoveCollector.remote(data_dir=os.path.join(working_dir, "data"))
    futures = [
        process_move.remote(move, collector)
        for move in moves
    ]
    results = ray.get(futures)

    print("Dataset generation complete")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()