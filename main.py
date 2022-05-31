# -*- coding: utf-8 -*-
""" Main script for the generation of UIB OOD dataset.

Written by: Miquel Miró Nicolau (UIB), 2022
"""
import argparse
import os

import cv2

import data_generation


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("output_folder", help="Folder to save the images", type=str)
    parser.add_argument("n_images", help="Number of images to generate", type=int)
    parser.add_argument("width", help="Width of the image to generate", type=int)
    parser.add_argument("height", help="Height of images to generate", type=int)

    args = parser.parse_args()

    folder = args.output_folder
    n_images = args.n_images
    size = (args.width, args.height)

    for id_img, img in enumerate(data_generation.get_random_images(n_images, size)):
        os.makedirs(folder, exist_ok=True)

        cv2.imwrite(os.path.join(folder, f"{id_img}.png"), img)

    return True


if __name__ == '__main__':
    main()
