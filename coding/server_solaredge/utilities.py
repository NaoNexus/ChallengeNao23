import time
import yaml


def getElapsedTime(startTime):
    elapsedTime = time.time() - startTime

    hours = elapsedTime // 360
    minutes = (elapsedTime - hours * 360) // 60
    seconds = (elapsedTime - hours * 360 - minutes * 60)

    return f'{int(hours)}h {int(minutes)}m {int(seconds)}s'


def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
