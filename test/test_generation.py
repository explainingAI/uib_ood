# -*- coding: utf-8 -*
""" Suite of tests for the generator of out of domain images.

Writen by: Miquel Miró-Nicolau (UIB), 2022.
"""
import unittest

import data_generation


class TestOODGenerator(unittest.TestCase):
    def test_generator_cte(self):
        iterator = iter(data_generation.get_random_images(10, (512, 512)))

        for i in range(1):  # Each of the example
            random_img = next(iterator)

        self.assertAlmostEqual(random_img.shape[0], 512)
        self.assertAlmostEqual(random_img.shape[1], 512)

    def test_generator_gauss(self):
        iterator = iter(data_generation.get_random_images(10, (512, 512)))

        for i in range(2):  # Each of the example
            random_img = next(iterator)

        self.assertAlmostEqual(random_img.shape[0], 512)
        self.assertAlmostEqual(random_img.shape[1], 512)

    def test_generator_speck(self):
        iterator = iter(data_generation.get_random_images(10, (512, 512)))

        for i in range(3):  # Each of the example
            random_img = next(iterator)

        self.assertAlmostEqual(random_img.shape[0], 512)
        self.assertAlmostEqual(random_img.shape[1], 512)

    def test_generator_sandp(self):
        iterator = iter(data_generation.get_random_images(10, (512, 512)))

        for i in range(4):  # Each of the example
            random_img = next(iterator)

        self.assertAlmostEqual(random_img.shape[0], 512)
        self.assertAlmostEqual(random_img.shape[1], 512)
