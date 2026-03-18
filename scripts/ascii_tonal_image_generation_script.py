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
example_filepath = "../ascii_example_art/ascii-art-leaffrog.txt"

# Open ascii art .txt file
img_ascii_artfile = open(example_filepath)

# read ascii art .txt file
ascii_art_string = img_ascii_artfile.read()

# Check file
# print(ascii_art_string)

# Find Image Dimensions (Height & Width)
image_height = len(ascii_art_string.splitlines())
image_width = len(ascii_art_string.splitlines()[0])

# Check Image Dimensions
# print(f"The image height is {image_height} and the image width is {image_width}")

# =============================================================================
# Reading/ Interpolating ASCII Art "Depth" through Character Visual Depth
# 
#   -  As the way the depth in ASCII art is made is generally variable, we 
#      need a shared grading system
#
# Paul Bourke's "Standard" ASCII Art Character Ramp (Black -> White):
# "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "
# souced at "https://paulbourke.net/dataformats/asciiart/"
#   -  We need to add a backslash \ before the " as otherwise the string is confused
# 
# what we need
#   -  A Function that takes an
#       -  Input: Ascii art file string, user color preference
#       -  Processes depth information based on Scale above and matches it 
#          to a tonal range of a user selected color
#       -  Output: Ascii PPM string raster
# =============================================================================

# Function to pixelize the ascii art
def pixelize_ascii(ascii_str, name):
    
    # Part 1
    # Define Header Variables
    image_ppm_header_type = "P3"

    image_width = len(ascii_str.splitlines()[0])
    image_height = len(ascii_str.splitlines()) * 2        # needs to be multiplied by 2 to account for text height (text is not square)

    image_max_color_value = 255

    image_header = f"{image_ppm_header_type}\n{image_width} {image_height}\n{image_max_color_value}\n"
    
    
    
    # Part 2
    # Color Selection Input
    def user_color_select(colors):
        
        # Declare Variables
        color_selected = []
        
        # User input
        user_color_selection = input("\nWhat color would you like to use today?\n")
        
        # While Loop Parsing and/ or Confirming Color Selection
        while len(color_selected) < 1:
            if user_color_selection.lower() in colors:
                color_selected = colors[user_color_selection.lower()]
            else:
                check_one = input("\nAre you sure you input that color name correctly? y or n\n* this is a simple system, typos will break it\n")
                if check_one == 'n':
                    user_color_selection = input("\nWhat color would you like to use today?\n")
                else:
                    check_two = input(f"\nIm sorry '{user_color_selection}' is not a color we have listed, would you like to retry, input the RGB code directly or Give up? 1 or 2 or 3\n  (1) Retry\n  (2) Input RGB\n  (3) Give Up\n")
                    if check_two == "1":
                        user_color_selection = input("\nWhat color would you like to use today?\n")
                    elif check_two == "2":
                        red_code = int(input("\nThe Red decimal code (0 - 255) in the RGB is\n"))
                        green_code = int(input("\nThe Green decimal code (0 - 255) in the RGB is\n"))
                        blue_code = int(input("\nThe Blue decimal code (0 - 255) in the RGB is\n"))
                        color_selected.append(red_code)
                        color_selected.append(green_code)
                        color_selected.append(blue_code)
                    else:
                        color_selected.append(None)
               
        # Return Color RGB Selection 
        return(color_selected)
    
    # Basic Color Selection Dictionary
    basic_colors_dict = {
        "red" : (255,0,0),
        "orange" : (255,128,0),
        "yellow" : (255,255,0),
        "green" : (0,255,0),
        "cyan" : (0,255,255),
        "blue" : (0,128,255),
        "dark blue" : (0,0,255),
        "purple" : (128,0,255),
        "pink" : (255,0,255),
        "hot pink" : (255,0,128),
        "grey" : (128,128,128),
        "black" : (0,0,0)
        }
    
    # Color Selection
    color_picker = user_color_select(basic_colors_dict)
    
    
    
    # Part 3
    # Create Color Swatch Dictionary
    # Define Base Variables
    character_ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    # Define Resulting empty dictionary
    color_range = {}
    n_steps = len(character_ramp)

    # for loop setting color range
    for i in range(n_steps):
        if n_steps % 2 ==0:
            if i == 0:
                r_code = 0
                g_code = 0
                b_code = 0
            elif i < (n_steps/2-1):
                r_code += (color_picker[0]) / (n_steps/2 - 1)
                g_code += (color_picker[1]) / (n_steps/2 - 1)
                b_code += (color_picker[2]) / (n_steps/2 - 1)
            elif i >= (n_steps/2):
                r_code += (255 - color_picker[0]) / (n_steps/2)
                g_code += (255 - color_picker[1]) / (n_steps/2)
                b_code += (255 - color_picker[2]) / (n_steps/2)
            else:
                r_code = color_picker[0]
                g_code = color_picker[1]
                b_code = color_picker[2]
        else:
            if i == 0:
                r_code = 0
                g_code = 0
                b_code = 0
            elif i < (n_steps/2):
                r_code += (color_picker[0]) / (n_steps/2)
                g_code += (color_picker[1]) / (n_steps/2)
                b_code += (color_picker[2]) / (n_steps/2)
            elif i >= (n_steps/2):
                r_code += (255 - color_picker[0]) / (n_steps/2)
                g_code += (255 - color_picker[1]) / (n_steps/2)
                b_code += (255 - color_picker[2]) / (n_steps/2)
            else:
                r_code = color_picker[0]
                g_code = color_picker[1]
                b_code = color_picker[2]
        
        color_range[character_ramp[i]] = [int(r_code),int(g_code),int(b_code)]
    
    
    
    
    # Step 4
    # Prepare Transform input string into ppm body
    # Define Output String
    ppm_output_str = ""
    
    # P3 PPM Row Loop function
    for row in ascii_str.splitlines():
        for i in range(2):          # print each line twice to make up for text height
            for pixel in row:
                if pixel in color_range.keys():
                    ppm_output_str += f"{color_range[pixel][0]} {color_range[pixel][1]} {color_range[pixel][2]} "
            ppm_output_str += "\n"
        
    
    
    
    # Part 5
    # writing out a file using python I/O
    with open(f"../image_outputs/{name}.ppm", "w") as ppm_file:
        
        ppm_file.write(image_header)
        
        ppm_file.write(ppm_output_str)
        print(f"\nAn image has been outputed to /image_outputs:\n\n  File Name: {name}.ppm\n  Image Height: {int(image_height/2)} pixels\n  Image Width: {image_width} pixels\n  Total Pixels: {image_height * image_width} pixels")




pixelize_ascii(ascii_art_string, "file_002")



