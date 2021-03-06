#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyBLNET',
    version='0.7.1',
    description='Automate web based communication with BL-NET to UVR1611',
    author='Niels Mündler',
    author_email='n.muendler@web.de',
    url='https://github.com/nielstron/pyblnet/',
    py_modules=['pyblnet'],
    packages=find_packages(),
    install_requires=['htmldom', 'requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Object Brokering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6'
    ],
    keywords='python uvr1611 blnet technische alternative',
    python_requires='>=3',
)
