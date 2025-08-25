#!/usr/bin/env python3

import unittest

def sort(width: int, height: int, length: int, mass: int):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError

    bulky = False
    heavy = False

    if width * height * length >= 1000000 \
            or width >= 150 \
            or height >= 150 \
            or length >= 150:
        bulky = True

    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return 'REJECTED'
    elif bulky or heavy:
        return 'SPECIAL'
    else:
        return 'STANDARD'


class TestSort(unittest.TestCase):
    def test_sort_not_bulky_not_heavy(self):
        self.assertEqual(sort(10, 10, 10, 1), 'STANDARD')
        self.assertEqual(sort(50, 50, 50, 10), 'STANDARD')

    def test_sort_bulky(self):
        self.assertEqual(sort(150, 10, 10, 1), 'SPECIAL')
        self.assertEqual(sort(10, 150, 10, 1), 'SPECIAL')
        self.assertEqual(sort(10, 10, 300, 1), 'SPECIAL')
        self.assertEqual(sort(10, 10, 10, 20), 'SPECIAL')
        self.assertEqual(sort(10, 10, 10, 21), 'SPECIAL')
    
    def test_sort_bulky_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), 'REJECTED')
        self.assertEqual(sort(101, 101, 101, 21), 'REJECTED')

    def test_sort_invalid(self):
        with self.assertRaises(ValueError):
            sort(-10, 10, 10, 10)

        with self.assertRaises(ValueError):
            sort(10, -10, 10, 10)

        with self.assertRaises(ValueError):
            sort(10, 10, -10, 10)

        with self.assertRaises(ValueError):
            sort(10, 10, 10, 0)

if __name__ == '__main__':
    unittest.main()
