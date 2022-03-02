import os


def resolve(filename):
    return '{0}\\assets\{1}'.format(os.path.dirname(os.path.abspath(__file__)), filename)
