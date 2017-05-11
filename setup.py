# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Import needed objects from setuptools, the Python package creation library
# recommended by PyPI
from setuptools import Extension, setup

# Create Extension object that contains info necessary to build cstringdist C
# extension module. The extra_compile_args argument is used to pass a -std=c99
# flag to the compiler, which ensures proper compilation on systems that don't
# default to the C99 standard (some of the included C code uses C99 syntax)
c_directory = 'stringdist/cstringdist/'
cstringdist = Extension(
    'cstringdist',
    sources=[
        c_directory + 'cstringdist.c',
        c_directory + 'levenshtein.c',
        c_directory + 'rdlevenshtein.c',
        c_directory + 'levenshtein_shared.c',
    ],
    extra_compile_args=['-std=c99'],
)

# Create dictionary that will be unpacked into keyword arguments and passed to
# the setup function used to generate the StringDist package. These are mostly
# self-explanatory (classifiers are tags used to filter packages on PyPI)
setup_args = {
    'name': 'StringDist',
    'version': '1.0.9',
    'description': 'This package provides the stringdist module, which'
                   ' includes several functions for calculating string'
                   ' distances. Under the hood, a C extension module is'
                   ' preferentially used for optimal performance, with an'
                   ' automatic fallback to a Python implementation.',
    'url': 'https://github.com/obulkin/string-dist',
    'author': 'Oleg Bulkin',
    'author_email': 'o.bulkin@gmail.com',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Libraries',
    ],
    'keywords': 'string metric string distance edit distance levenshtein'
                ' damerau-levenshtein optimal string alignment distance',
    'packages': ['stringdist', 'stringdist/pystringdist'],
    'ext_modules': [cstringdist],
}

# Try to generate the package by calling the setup function. If compilation of
# the C extension module fails, a SystemExit exception will be raised. This is
# caught and used a signal to fall back to the Python implementation by
# printing an appropriate message, removing the extension module from
# setup_args, and calling setup again
try:
    setup(**setup_args)
except SystemExit:
    print(
        'Your environment may not support the use of C extensions. Falling'
        ' back to Python implementation.'
    )
    del setup_args['ext_modules']
    setup(**setup_args)
