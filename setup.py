"""
A setuptools based on setup module for MADIS.
"""

# Always prefer setuptools over distutils
import os
from setuptools import setup

setup(
    name="m1ch3al-pyqt5-widgets",
    version="0.1",
    description="A PyQt5 useful widgets.",
    # The project's main homepage.
    url="https://github.com/m1ch3al/pyqt5-widgets.git",
    # Author details
    author="Renato Sirola",
    author_email="renato.sirola@gmail.com",
    # Choose your license
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    # What does your project relate to?
    keywords="graphics, user interface, gui, pyqt5 qt, python3",
    include_package_data=False,
    install_requires=[
        'setuptools',
        'pyqt5',
    ],
    packages=[
        'm1ch3al',
        'm1ch3al.pyqt5_widgets',
        'm1ch3al.pyqt5_widgets.tests',
        'm1ch3al.pyqt5_widgets.tests.thermometer'
    ]
)

