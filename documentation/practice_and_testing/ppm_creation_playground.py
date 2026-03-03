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

image_width = 5
image_height = 3

image_max_color_value = 255

image_header = f"{image_ppm_header_type}\n{image_width} {image_height}\n{image_max_color_value}\n"


# =============================================================================
# As far as I understand
#   -  A ppm is built with a Header and then a sort of Array
#       -  The array for P3 is compossed of 3 ascii numbers from 0 to 255 representing RGB
#       -  The 3 numbers and consequent numbers seperated by whitespaces
#       -  P3 structure can be printed in console but visualization only possible in output
# =============================================================================

# Define Color Variable
red = 0
green = 0
blue = 0

# P3 PPM Loop function
for row in range(image_height):
    row_string = ""
    
    for pixel in range(image_width):
        if red < 255:
            row_string += f"{red} {green} {blue} "
            red += 51
        elif green < 255:
            row_string += f"{red} {green} {blue} "
            green += 51
        elif blue < 255:
            row_string += f"{red} {green} {blue} "
            blue += 51
        else:
            red = 0
            green = 0
            blue = 0
            row_string += f"{red} {green} {blue} "
    print(row_string)


# writing out a file using python I/O
with open("../../image_outputs/temp_output.ppm", "w") as ppm_file:
    
    ppm_file.write(image_header)
    print(f"image header values:\n{image_header}have been added to the PPM file")
    
    for row in range(image_height):
        row_string = ""
        
        for pixel in range(image_width):
            if red < 255:
                row_string += f"{red} {green} {blue} "
                red += 51
            elif green < 255:
                row_string += f"{red} {green} {blue} "
                green += 51
            elif blue < 255:
                row_string += f"{red} {green} {blue} "
                blue += 51
            else:
                red = 0
                green = 0
                blue = 0
                row_string += f"{red} {green} {blue} "
        ppm_file.write(row_string+"\n")
        print(f"row number {row + 1} has been added to the PPM file")