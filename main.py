import logging

from data_generator import DataGenerator

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data_gen = DataGenerator(target_dir="data")
    data_gen.generate()
