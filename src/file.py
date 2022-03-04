import os


def resolve(filename):
    """
    Resolves file path independent of path of command execution 
    """
    return '{0}\\assets\{1}'.format(os.path.dirname(os.path.abspath(__file__)), filename)
