import os


def create_dir(name):
    parent = os.path.dirname(os.getcwd())
    path = os.path.join(parent, name)
    if not os.path.exists(path):
        os.mkdir(os.path.join(path))
    return path
