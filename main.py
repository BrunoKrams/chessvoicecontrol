import os

import data_generator

if __name__ == "__main__":
    target_dir = os.path.join(os.path.dirname(__file__), "results/wav")
    print(f"Storing generated wavs in {target_dir}")
    data_generator = data_generator.DataGenerator(target_dir)
    data_generator.run()