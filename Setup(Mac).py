from setuptools import setup

APP = ['PROG FJU.py']

DATA_FILES = ['fichiers', 'images', 'logo', 'sons', 'license.txt']

OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)