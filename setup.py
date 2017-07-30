#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='blinkt',
    version='0.1dev',
    packages=find_packages(),
    install_requires=['arcade'],
    description="Emulates blinkt api on non pi devices with a small ui.",
    long_description=open('README.md').read(),
)