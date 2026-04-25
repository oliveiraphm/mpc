from pathlib import Path
from ch03.recipe_11 import distances

if __name__ == "__main__":
    for trip in 'trip_1.csv', 'trip_2.csv':
        distances(Path('data') / trip)