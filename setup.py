from setuptools import setup, find_packages

setup(
    name='smartformatter',
    version='0.1',
    packages=find_packages(),
    install_requires=['inflect'],
    author='jaswanthi',
    description='Utility functions for smart formatting of names,phones,numbers.',
)