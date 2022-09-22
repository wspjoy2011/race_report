"""
Get base dir module
Return base dir of package
"""
import os


def get_base_dir():
    if 'racing_data' not in os.listdir():
        os.chdir('..')
    path = os.getcwd()
    return path
