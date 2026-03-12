#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:37:26 2026

Color Selection Trial

 - User Selects color in simple manner (basic input) with main 
   choices being typeable (eg."Black" or "Red")
 - Maybe Second function to be able to directly input RGB values 
   (since no Libraries)
 
Color Tonal Depth affecting RGB

 - Affect user Selected Color to create n number (number of unique 
   characters on ascii art) of tonal variations in RGB

@author: seanschallberger
"""

# =============================================================================
# As I dont think I'm supposed to use other libraries for this project, my choices for
# the color selection system is to either
# 
#   -  Create a Dictionary of as many color as possible to act as selectable colors
#       -  if a color outside of the selection is requested then ask the used to pick
#          between picking a new color or inputing the RGB in themselves
#       -  Base color picker:
#          https://www.rapidtables.com/web/color/RGB_Color.html
#   -  Use a .txt file input or .csv with a color directory like those on kaggle
#       -  considering on using
#          https://www.kaggle.com/datasets/avi1023/color-names?resource=download
#
# =============================================================================

# Color Selection Dictionary
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

# If statement function to get user color selection 
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

# Test Function
# print(user_color_select(basic_colors_dict))


# =============================================================================
# If I'm allowed to at least parse a csv file then I could do:
# =============================================================================

# Define Variables
colors_csv_filepath = "../color_dataset/color_names_kaggle.csv"
colors_dict = {}

# Open and read CSV file
colors_csv = open(colors_csv_filepath, "r").read()

# Loop to turn CSV text into a Dictionary
for line in colors_csv.splitlines():
    color_line = line.split(",")
    color_line[0] = color_line[0].strip(('"'))
    
    if color_line[0] != "Name":
        # Declare Color Name String and RGB Values
        color_name = color_line[0].lower()
        color_r = int(color_line[2])
        color_g = int(color_line[3])
        color_b = int(color_line[4])
        
        # Add Dictionary Entries
        colors_dict[color_name] = [color_r, color_g, color_b]


# Test Color Picker Function
# print(user_color_select(colors_dict))


# =============================================================================
# Make n number tonal variations of the selected color
# =============================================================================

# Color Picker Test Variable
color_picker = user_color_select(basic_colors_dict)

# Define Variables
n_steps = 11   # TONAL Variation number (maybe will turn later input an input statement)

# Define Resulting empty dictionary
color_range = {}

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
    
    color_range[i] = [int(r_code),int(g_code),int(b_code)]

# Test Color Range print
# print(color_range)


# =============================================================================
# Test PPM creation
# =============================================================================

# Define Header Variables
image_ppm_header_type = "P3"

image_width = n_steps
image_height = 1

image_max_color_value = 255

image_header = f"{image_ppm_header_type}\n{image_width} {image_height}\n{image_max_color_value}\n"

# Define Output String
ppm_output_str = ""

# Color swatch test print Variable (essentially placeholder of the input text file)
color_swatch = [i for i in range(n_steps)]

# Turn color swatch list into ppm data
for i in range(len(color_swatch)):
    if color_swatch[i] in color_range.keys():
        ppm_output_str += f"{color_range[color_swatch[i]][0]} {color_range[color_swatch[i]][1]} {color_range[color_swatch[i]][2]} "

# Test output string
# print(ppm_output_str)
        

# writing out a file using python I/O
with open("../../image_outputs/tonal_test.ppm", "w") as ppm_file:
    
    ppm_file.write(image_header)
    print(f"The image header values:\n{image_header}have been added to the PPM file\n")
    
    ppm_file.write(ppm_output_str)
    print(f"A total of {len(ppm_output_str.splitlines())} lines have been added to the PPM file")












