#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:13:02 2026

Project: ascii_tonal_generator

Prime Targets:
    - Clean up v1 Function logic
        - Split each logi part of the function into seperate functions
        - Have 1 function call all other functions thus giving us cleaner code
    - Add other color ways

@author: seanschallberger
"""

# =============================================================================
# Function 1: Welcome Sequence 1:
#   
#   - Pick and design ascii art filepath
#       - Pick either an example Test file or user's own file
# =============================================================================

def pick_file_name():
    
    # Define Function 1 Variables
    test_file_names = ["ascii-art-leaffrog", "ascii-art-smallbanana", "ascii-art-treefrog", "ascii-art-treefrog copy"]
    chosen_filepath = ""
    
    # Start Up Statement
    run_check = input("Hello User!\n\nDo you want to try generating an Ascii Tonal Artwork?\n  y  - yes\n  n  - no\n\nInput:\n")
    
    # File Name/ Path defining    -->  Returns file filepath from here
    if run_check.lower() == "n":
        print("\nOkay! Till next time!")
        return None
    else:
        test_or_custom = input("\nAmazing! do you want to generate one using one of the example test files or your own ascii art file??\n\nPlease Input 0/1\n  0  -  Use a test file\n  1  -  Use your own file\n\nInput:\n")
        if test_or_custom == "0":
            print("\nOkay input the file number you want to test!")
            for i in range(len(test_file_names)):
                print(f'  {i}  - "{test_file_names[i]}"')
            chosen_filepath = "../ascii_example_art/" + test_file_names[int(input("\nInput:\n"))] + ".txt"
        else:
            print("\nOkay lets do this! please make sure the file is in the same directory as this '.py' file and input your '.txt' file name!")
            custom_filepath = input("\nWhats your file name?\n")
            if ".txt" in custom_filepath:
                chosen_filepath = custom_filepath
            else:
                chosen_filepath = custom_filepath + ".txt"
    
    # Return the chosen file path
    return chosen_filepath


# =============================================================================
# Function 2: File Open and File Check Function
#   
#   - finds and opens file based on File path input
#   - Check File compatability with code
#       * Currently the ascii tonal art needs to be a set width and height throughout the artwork (no Free Form ascii Art) as the code needs to create a properly sized ppm file
# =============================================================================

def file_open(filepath):
    
    # Open and Read Ascii Art File
    file_contents_string = open(filepath).read()
    file_compatibility = True
    non_compatible_rows = []
    
    # Check File Compatibility
    # Find Image Dimensions (Height & Width)
    image_height = len(file_contents_string.splitlines())
    image_width = len(file_contents_string.splitlines()[0])
    
    # Check that all rows have same width and thus file is compatible
    for row in range(image_height):
        if len(file_contents_string.splitlines()[row]) != image_width:
            non_compatible_rows.append(str(row))
            file_compatibility = False
    
    # Designate Compatibility
    if file_compatibility == True:
        # Return the file Contents
        return file_contents_string
    
    else:
        print(f"I'm sorry it seems the file you picked is not compatible with this current system version.\nPlease make sure all rows are the same length as the top row which has a length of {image_width} characters.\n\nBe advised your file failed on line(s) {', '.join(non_compatible_rows)}")
        return None
    



# =============================================================================
# Function Test Section (Temp)
# 
# **EDITS**
#   - Realized that ill need failsafes between the functions otherwise whole program can fail  
#       - Fail safes using if statements work but require None type returns and can still give certain errors
#       - Try and Except may be best used around certain sections
# =============================================================================


# Test Function 1 - Returns Filepath 
test_filepath = pick_file_name()

# Function 1 logic gate
if test_filepath != None:
    
    # Test print 1
    print("\n" + test_filepath)
        
    # Test Function 2 - Returns file contents
    test_file_contents = file_open(test_filepath)
    
    # Function 2 Logic Gate
    if test_file_contents != None:
        
        # Test print 2
        print("\n" + test_file_contents)