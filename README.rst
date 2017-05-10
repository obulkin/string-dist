==========
StringDist
==========

This package provides the ``stringdist`` module, which includes functions for 
calculating raw and normalized versions of the following string distance 
measurements:

* Levenshtein distance
* Restricted Damerau-Levenshtein distance (a.k.a. optimal string alignment 
  distance)

For optimal performance, the package compiles and uses a C extension module 
under the hood, but a Python implementation is included as well and will 
automatically be used if C extensions are not supported by the system 
(e.g. when the selected interpreter is PyPy).

Installation
============

To install this package, just use pip::

    pip install StringDist

Usage
=====

To use the package, simply import the ``stringdist`` module and call the 
desired function, passing in two strings::

    import stringdist
    stringdist.levenshtein('test', 'testing')

The available functions are as follows:

* ``levenshtein``
* ``levenshtein_norm``
* ``rdlevenshtein``
* ``rdlevenshtein_norm``

Raw distances assume that every allowed operation has a cost of ``1``. 
Normalized distances are floats in the range ``[0.0, 1.0]``, where ``0.0`` 
always corresponds to a raw value of ``0`` and ``1.0`` always corresponds to 
the length of the longer string, i.e. the biggest possible raw value.

**Note**: The restricted Damerau-Levenshtein distance is not a true distance 
metric because it does not satisfy the 
`triangle inequality <https://en.wikipedia.org/wiki/Triangle_inequality>`_. 
This makes it a poor choice for applications that involve evaluating the 
similarity of more than two strings, such as clustering.

Bugs and Requests
=================

Please use `GitHub Issues <https://github.com/obulkin/string-dist/issues>`_ 
for bugs and feature requests, checking first to make sure you're not creating 
a duplicate issue.

Contributing
============

Pull requests are welcome. Please discuss your plans first by creating a 
GitHub issue and use good coding style. For Python, this means following the 
rules laid out in PEP 8 and other relevant PEPs. If in doubt, use a linter 
like `Pylint <https://www.pylint.org>`_.

To run unit tests::

    git clone https://github.com/obulkin/string-dist.git {directory}
    cd {directory}
    python setup.py install
    python -m unittest -v test_stringdist

You can run tests without installing the package, but this will always cause 
the Python implementation to be used as the C variant has to be compiled 
first. By the same token, any changes to the C code will require recompilation 
before showing up in the tests, which can be handled by running 
``python setup.py install`` again.

Contributors
============

* Oleg Bulkin <o.bulkin@gmail.com>
