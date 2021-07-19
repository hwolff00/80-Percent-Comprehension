import os

def find_dir(name):
    parent = os.path.dirname(os.getcwd())
    path = os.path.join(parent, name)
    return path
