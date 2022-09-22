from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='collection_framework_wspjoy2011',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'attrs==22.1.0',
        'colorama==0.4.5',
        'coverage==6.4.4',
        'iniconfig==1.1.1',
        'packaging==21.3',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pyparsing==3.0.9',
        'pytest==7.1.3',
        'tomli==2.0.1',
    ]
)