from pathlib import Path
from ch03.recipe_11 import distances

if __name__ == "__main__":
    distances(Path('data') / 'trip_1.csv')