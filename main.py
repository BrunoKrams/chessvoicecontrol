import concurrent
import logging
import os

from datafiles_generator import DataGenerator
from model.moves import all_moves
from model.moves.move import Move


def generate_move(target_dir, move):
    generator = DataGenerator(target_dir)
    generator.generate(move)
    return move.identifier()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(script_dir, "data")
    logging.info(f"Target dir: {target_dir}")
    cpu_count = os.cpu_count()
    used_cpus = cpu_count -1
    logging.info(f"{cpu_count} cores detected. Using {used_cpus} of them")

    os.makedirs(target_dir, exist_ok=False)
    moves = all_moves.all()

    total = len(moves)
    logging.info(f"Generating data for {total} moves")

    with concurrent.futures.ProcessPoolExecutor(
            max_workers=used_cpus
    ) as executor:
        futures = [executor.submit(generate_move, target_dir, move) for move in moves]
        for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            try:
                move_id = future.result()
                logging.info(f"[{done}/{total}] Finished '{move_id}' — {total - done} left")
            except Exception:
                logging.exception(f"[{done}/{total}] Data generation failed — {total - done} left")

