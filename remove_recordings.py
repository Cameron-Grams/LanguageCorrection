import os

recordings = "./recordings/"
files = os.listdir(recordings)
for file in files:
    os.remove(recordings + file)
