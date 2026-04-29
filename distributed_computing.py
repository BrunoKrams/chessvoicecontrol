import os
import ray

import wav_generator
from wav_generator import WavGenerator


@ray.remote
class MoveCollector:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=False)

    def write_move(self, move_id, wavs):
        move_dir = os.path.join(self.data_dir, move_id)
        os.makedirs(move_dir, exist_ok=False)

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
    wav_gen = WavGenerator()
    wavs = wav_gen.generate(move)
    move_id = move.identifier()
    return collector.write_move.remote(
        move_id,
        wavs
    )

def main():
    ray.init(address="auto")
    moves = [f"move_spec_{i}" for i in range(20)]
    collector = MoveCollector.options(
        resources={"node:__head__": 0.01}
    ).remote()
    futures = [
        process_move.remote(move, i, collector)
        for i, move in enumerate(moves)
    ]
    results = ray.get(futures)
    print("Dataset generation complete.")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()