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
img_ascii_artfile = open(example_filepath)

# read ascii art .txt file
ascii_art_string = img_ascii_artfile.read()

# Check file
print(ascii_art_string)

# Find Image Dimensions (Height & Width)
image_height = len(ascii_art_string.splitlines())
image_width = len(ascii_art_string.splitlines()[0])

# Check Image Dimensions
print(f"The image height is {image_height} and the image width is {image_width}")

# =============================================================================
# Reading/ Interpolating ASCII Art "Depth" through Character Visual Depth
# 
#   -  As depth in ASCII art is generally
#
# Paul Bourke's "Standard" ASCII Art Character Ramp (Black -> White):
# "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "
# souced at "https://paulbourke.net/dataformats/asciiart/"
# 
# what we need
#   -  A Function that takes an
#       -  Input: Ascii art file string, user color preference
#       -  Processes depth information based on Scale above and matches it 
#          to a tonal range of a user selected color
#       -  Output: Ascii PPM string raster
# =============================================================================

# Function to pixelize the ascii art
def pixelize_ascii(ascii_str, color):
    