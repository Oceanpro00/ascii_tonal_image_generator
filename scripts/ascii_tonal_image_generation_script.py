#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:51:07 2026

Project: ascii_tonal_image_generator

@author: seanschallberger
"""

# =============================================================================
# Open and read the Ascii Art File
# =============================================================================

# Define Filepaths
example_filepath = "../ascii_example_art/ascii-art-smallbanana.txt"

# Open ascii art .txt file
img_ascii_file = open(example_filepath)

# test read ascii art .text file
print(img_ascii_file.read())

