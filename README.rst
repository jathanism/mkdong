######
mkdong
######

A Python module and command-line utility for printing dongs.  

Installation
============

Using pip::

    $ pip install mkdong

From source::

    $ git clone https://github.com/cfralick/mkdong.git  
    $ cd mkdong  
    $ python setup.py install  

Usage
=====

Command line::

    $ mkdong 5

Python::

    >>> import mkdong     
    >>> mkdong.dong(5)    
    '( )/( )=====D'    
    >>> mkdong.dong(5, wide=True)
    >>> '( )/( )/////D'
    >>> mkdong.dong(5, climax=True)
    >>> '( )/( )=====D ~~~~'

Help
====

::

    $ mkdong --help
    usage: mkdong [-h] [-w] [-c] [-v] <length>

    Prints a dong.

    positional arguments:
      <length>       The desired dong length.

    optional arguments:
      -h, --help     show this help message and exit
      -w, --wide     Make a wide, thick dong.
      -c, --climax   Makes the dong climax.
      -v, --version  Print version and exit.

    mkdong 7.0

Development
===========

Running tests::

    $ pip install -r requirements.txt
    $ py.test -v tests/
