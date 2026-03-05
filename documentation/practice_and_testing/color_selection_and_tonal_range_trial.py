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

# Declare Variables
color_selected = []

# Color Selection Dictionary
colors_dict = {
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

# User input
user_color_selection = input("\nWhat color would you like to use today?\n")

# While Loop Parsing and/ or Confirming Color Selection
while len(color_selected) < 1:
    if user_color_selection.lower() in colors_dict:
        color_selected = colors_dict[user_color_selection.lower()]
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
       
# Test Color RGB Selection 
print(color_selected)