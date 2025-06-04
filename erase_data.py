import os

def erase_data(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        os.remove(path)

originals_directory = "data/originals"
updates_directory = "data/updates"

erase_data(originals_directory)
erase_data(updates_directory)
