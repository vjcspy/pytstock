import time
from termcolor import colored

import typer
from rich.progress import track

from modules.core.logging.logger import Logger


def main():
    logger = Logger()
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1

    logger.info(f'Processed {colored(total,"blue")} things.')


if __name__ == "__main__":
    typer.run(main)
