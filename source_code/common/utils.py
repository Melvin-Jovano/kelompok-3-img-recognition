import os

def getListDir(dir: str):
    return [x for x in os.listdir(dir) if not any(substring in x for substring in ('.DS_Store', '.placeholder'))]