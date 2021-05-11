"""Setuptools for python

This is the standard way to create a package out of a python project.
This is done so the python modules can interact with eachother using
the python 'dot' notation.
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-pkg-TheOGZer0",
    version="0.0.1",
    author="Jimmy Bierenbroodspot",
    author_email="jim12.brood@gmail.com",
    description="A game of snake but multiplayer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheOGZer0/multiplayer-snake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD-3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
