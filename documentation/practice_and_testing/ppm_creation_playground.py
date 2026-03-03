#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:23:16 2026

PPM File creation Playaround

Learning from - 
ppm header structure: https://solarianprogrammer.com/2017/10/25/ppm-image-python-3/
ppm file structure: https://netpbm.sourceforge.net/doc/ppm.html

@author: seanschallberger
"""

# =============================================================================
# PPM Creation notes:
# 
#   Starts with a HEADER that consists of
#   -  A magic number: P3 or P6
#       -  P3 is in regular ASCII text format (so bigger/ slower)
#       -  P6 is in raw binary format (so smaller/ faster)
#   -  A Whitespace Character " " or TAB or LB
#   -  The Width and Height of the image: 200 600
#       -  separated by a white space
#   -  A Whitespace Character " " or TAB or LB
#   -  The Maximum Color Value: 255
#       -  typically 255
#
#   example:
#   P3
#   200 600
#   255
# =============================================================================

# Define Header Variables
image_ppm_header_type = "P3"

image_width = 10
image_height = 10

image_max_color_value = 255

image_header = f"{image_ppm_header_type}\n{image_width} {image_height}\n{image_max_color_value}\n"


# =============================================================================
# As far as I understand
#   -  A ppm is built with a Header and then a sort of Array
#       -  The array for P3 is compossed of 3 ascii numbers from 0 to 255 representing RGB
#       -  The 3 numbers and consequent numbers seperated by whitespaces
#       -  P3 structure can be printed in console but visualization only possible in output
# =============================================================================

# Color Gradient Function
def color_gradient(image_height, image_width):

    # Define Color Variable
    red = 0
    green = 0
    blue = 0

    # Define Variables
    pixel_count = image_height * image_width
    color_steps = 765 / pixel_count
    ppm_string = ""
    progress = 0
    

    # P3 PPM Row Loop function
    for row in range(image_height):
        for pixel in range(image_width):
            progress += color_steps
            if progress < 255:
                red = int(progress)
                ppm_string += f"{red} {green} {blue} "
            elif progress < 510:
                red = 255
                green = int(progress) - 255
                ppm_string += f"{red} {green} {blue} "
            else:
                red = 255
                green = 255
                blue = int(progress) - 510
                ppm_string += f"{red} {green} {blue} "
        ppm_string += "\n"
    
    return ppm_string


# Test output
for i in range(image_height):
    print(color_gradient(image_height, image_width))

# writing out a file using python I/O
with open("../../image_outputs/temp_output.ppm", "w") as ppm_file:
    
    ppm_file.write(image_header)
    print(f"The image header values:\n{image_header}have been added to the PPM file\n")
    
    ppm_data = color_gradient(image_height, image_width)
    ppm_file.write(ppm_data)
    print(f"A total of {len(ppm_data.splitlines())} lines have been added to the PPM file")