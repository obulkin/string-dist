from setuptools import Extension, setup

c_directory = 'stringdist/cstringdist/'
cstringdist = Extension(
    'cstringdist',
    sources=[
        c_directory + 'cstringdist.c',
        c_directory + 'levenshtein.c',
        c_directory + 'rdlevenshtein.c',
        c_directory + 'levenshtein_shared.c',
    ],
)

setup_args = {
    'name': 'StringDist',
    'version': '1.0.0',
    'description': 'This package provides the stringdist module, which'
                   ' includes several functions for calculating string'
                   ' distances. Under the hood, a C extension module is'
                   ' preferentially used for optimal performance, with an'
                   ' automatic fallback to a Python implementation.',
    'url': '',
    'author': 'Oleg Bulkin',
    'author_email': 'o.bulkin@gmail.com',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: C',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6.1',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
    'keywords': 'string metric string distance edit distance levenshtein'
                ' damerau-levenshtein optimal string alignment distance',
    'packages': ['stringdist'],
    'ext_modules': [cstringdist],
}

try:
    setup(**setup_args)
except SystemExit:
    print(
        'Your environment may not support the use of C extensions. Falling'
        ' back to Python implementation.'
    )
    del setup_args['ext_modules']
    setup(**setup_args)
