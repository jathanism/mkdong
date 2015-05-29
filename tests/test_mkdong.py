import unittest
from mkdong.mkdong import mkdong, MAXLEN
from argparse import ArgumentError


class MkdongTestCase(unittest.TestCase):

    def setUp(self):
        self.default_dong = mkdong(1, False)
        self.maxlen = MAXLEN
        self.dong_too_long = MAXLEN + 1

    def tearDown(self):
        self.default_dong = None
        self.maxlen = 0
        self.dong_too_long = None

    def test_dong_is_dong(self):
        dong = '( )/( )=D'
        self.assertEqual(mkdong(1, False), dong)

    def test_wide_dong_is_wide(self):
        dong = '( )/( )/D'
        self.assertEqual(mkdong(1, True), dong)

    def test_microdong_is_still_dong(self):
        micro = '( )/( )D'
        self.assertEqual(mkdong(0, False), micro)

    def test_wide_thin_microdongs_same(self):
        self.assertEqual(mkdong(0, False), mkdong(0, True))

    def test_climaxing_dong_shows_load(self):
        self.assertEqual(mkdong(1, False, True), self.default_dong + ' ~~~~')

    def test_non_int_dong_length_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong('penis', True)

    def test_superfluous_int_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong(10, False, False, 20)

    def test_superfluous_str_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong(10, False, False, 'cock')
