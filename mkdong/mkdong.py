#!/usr/bin/env python

"""
Prints a dong of a specific length.
"""


import os
import sys
import argparse


__author__ = 'Jathan McCollum, Mark Ellzey Thomas, Clint Fralick'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__version__ = '6.1'


# Static immutable penis parts
BALL = '( )'
HEAD = 'D'
THIN = '='
WIDE = '/'
CLIMAX = ' ~~~~'

ENV_VAR_NAME = 'MEGADONG'
DEFAULT_MAXLEN = 40

MAXLEN = os.environ.get(ENV_VAR_NAME) or DEFAULT_MAXLEN


def parse_args():
    parser = argparse.ArgumentParser(
        description='Prints a dong.',
        prog='mkdong',
        epilog='mkdong %s' % __version__
    )

    parser.add_argument('length',
                        metavar='l',
                        type=int,
                        help='the desired dong length')
    parser.add_argument('-w',
                        '--wide',
                        action='store_true',
                        help='make a wide, thick dong')
    parser.add_argument('-c',
                        '--climax',
                        action='store_true',
                        help='makes the dong climax')
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s ' + __version__,
                        help='print version and exit')
    dong_args = parser.parse_args()

    if dong_args.length > MAXLEN:
        parser.error(
            "error: a %s\" dong is too big! cannot be longer than %s\"!" %
            (dong_args.length, MAXLEN)
        )

    return (dong_args.length, dong_args.wide, dong_args.climax,)


def mkshaft(length, width):
    w = WIDE if width else THIN
    return _mk_dong_part(w, length, '')


def mkballs(balls=2):
    return _mk_dong_part(BALL, balls, '/')


def _mk_dong_part(v, r, d):
    return d.join([v for x in xrange(r)])


def _mk_dong(b, s, h, c=None):
    if c:
        d = ''.join([b, s, h, CLIMAX])
    else:
        d = ''.join([b, s, h])
    return d


def mkdong(length, width, climax=None):
    """Prints a dong of ``length`` length."""
    shaft = mkshaft(length, width)
    balls = mkballs()
    return _mk_dong(b=balls, s=shaft, h=HEAD, c=climax)


def main():
    length, width, climax = parse_args()

    try:
        dong = mkdong(length=length, width=width, climax=climax)
    except ValueError as ronjeremy:
        sys.exit(str(ronjeremy))
    else:
        os.system('echo "%s"' % dong)
