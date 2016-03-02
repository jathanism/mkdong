#!/usr/bin/env python

"""
Prints a dong of a specific length, width, and climax.
"""


from collections import namedtuple
import os
import sys
import argparse

from .version import __version__


__author__ = 'Jathan McCollum, Mark Ellzey Thomas, Clint Fralick'
__maintainer__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'


# Static immutable penis parts
BALL = '( )'
HEAD = 'D'
SHAFT_THIN = '='
SHAFT_WIDE = '/'
CLIMAX = ' ~~~~'

ENV_VAR_NAME = 'MEGADONG'
NUM_BALLS = 2
DEFAULT_MAXLEN = 40

MAXLEN = os.environ.get(ENV_VAR_NAME) or DEFAULT_MAXLEN


#: Used to store dong-making information
DongTuple = namedtuple('DongTuple', 'length wide climax')


def parse_args():
    """
    Parses args and returns a ``DongTuple``.

    :returns:
        `~mkdong.DongTuple`
    """
    parser = argparse.ArgumentParser(
        description='Prints a dong.', prog='mkdong',
        epilog='mkdong %s' % __version__
    )

    parser.add_argument(
        'length',
        metavar='<length>',
        type=int,
        help='The desired dong length.'
    )
    parser.add_argument(
        '-w', '--wide',
        action='store_true',
        help='Make a wide, thick dong.'
    )
    parser.add_argument(
        '-c', '--climax',
        action='store_true',
        help='Makes the dong climax.'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s ' + __version__,
        help='Print version and exit.'
    )
    dong_args = parser.parse_args()

    if dong_args.length > MAXLEN:
        parser.error(
            # "error: a %s\" dong is too big! cannot be longer than %s\"!" %
            'Soul brother, too beaucoup! (Cannot be longer than %s.)' % MAXLEN
        )

    return DongTuple(dong_args.length, dong_args.wide, dong_args.climax)


def mkshaft(length, wide=False):
    """
    Generate the shaft.

    :param length:
        Desired length

    :param wide:
        Wide or no?

    :returns:
        Shaft
    """
    shaft = SHAFT_WIDE if wide else SHAFT_THIN
    return _mk_dong_part(shaft, length, '')


def mkballs(balls=NUM_BALLS):
    """
    Generate the balls.

    :param balls:
        Number of balls

    :returns:
        Balls
    """
    return _mk_dong_part(BALL, balls, '/')


def _mk_dong_part(value, num_items, delimiter):
    """
    Join dong parts together.

    :param value:
        Dong part value

    :param num_items:
        Dong part repetitions

    :param delimiter:
        Dong part delimiter

    :returns:
        Dong part
    """
    return delimiter.join(value for _ in xrange(num_items))


def construct_dong(balls, shaft, head, climax=False):
    """
    Construct the dong.

    :param balls:
        Balls

    :param shaft:
        Shaft

    :param head:
        Head

    :param climax:
        Climax or no?

    :returns:
        Dong string
    """
    dong_parts = [balls, shaft, head]
    if climax:
        dong_parts.append(CLIMAX)

    return ''.join(dong_parts)


def mkdong(length, wide=False, climax=False):
    """
    Returns a fully constructed dong.

    :param length:
        Desired length

    :param wide:
        Wide or no?

    :param climax:
        Whether to climax

    :returns:
        Dong
    """
    shaft = mkshaft(length, wide)
    balls = mkballs()
    head = HEAD
    return construct_dong(balls, shaft, head, climax)


def main():
    """The Main Event."""
    length, wide, climax = parse_args()

    try:
        dong = mkdong(length=length, wide=wide, climax=climax)
    except ValueError as ronjeremy:
        sys.exit(str(ronjeremy))
    else:
        print dong
