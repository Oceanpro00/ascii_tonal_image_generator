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
    test_file_names = ["ascii-art-leaffrog", "ascii-art-smallbanana", "ascii-art-treefrog"]
    chosen_filepath = ""
    
    # Start Up Statement
    run_check = input("Hello User!\n\nDo you want to try generating an Ascii Tonal Artwork?\n  y  - yes\n  n  - no\n\nInput:\n")
    
    # File Name/ Path defining    -->  Returns file filepath from here
    if run_check.lower() == "n":
        print("\nOkay! Till next time!")
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
    
    return chosen_filepath


# =============================================================================
# Function 2: File Open and File Check Function
#   
#   - finds and opens file based on File path input
#   - Check File compatability with code
#       - Currently ascii tonal art needs to be a set width and height throughout the artwork (no Free Form ascii Art)
# =============================================================================



# =============================================================================
# Function Test Section (Temp)
# =============================================================================

# Test Function 1 - Returns Filepath 
test_filepath = pick_file_name()
print("\n" + test_filepath)
