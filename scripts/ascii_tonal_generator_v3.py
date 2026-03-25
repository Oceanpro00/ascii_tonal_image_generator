#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:48:24 2026

Project: ascii_tonal_generator

Prime Targets:
    - Clean up v2 color systems
        - Clean up how functions are called
    - Add new Color Systems
        - Restructure and rename the v2 basic to Mono Tone
        - Create Duo Tone
        - Create Tri Tone
        - Create Posterize

@author: seanschallberger
"""

# =============================================================================
# Function 1: Welcome Sequence:
#   
#   - Pick and designate an ascii art filepath (example / custom)
#   - Designate a File name
#   
# Output:
#   
#   - Name
#   - Filepath
# =============================================================================

def pick_file_path():
    
    # Define Function 1 Variables
    test_file_names = ["ascii-art-treefrog", "ascii-art-sunset", "ascii-art-chameleon", "ascii-art-geometric-circle", "ascii-art-marilyn-monroe"]
    chosen_filepath = ""
    
    # Start Up Statement
    run_check = input("Hello User!\n\nDo you want to try generating an Ascii Tonal Artwork?\n  y  - yes\n  n  - no\n\nInput:\n")
    
    # File Name/ Path defining    -->  Returns file filepath from here
    if run_check.lower() == "n":
        print("\nOkay! Till next time!")
        return None, None
    else:
        
        # Designate Name to Kick off
        name = input("\nThats awesome! What would you like to name the file?\n\nInput:\n")
        
        # First System Fork
        test_or_custom = input("\nIncredible name! Do you want to generate one using one of our example test files or your own ascii art file??\n\nPlease Input 0/1\n  0  -  Use a test file\n  1  -  Use your own file\n\nInput:\n")
        
        # Ensure Correct Input
        while test_or_custom not in ["0","1"]:
                test_or_custom = input(f"\n{test_or_custom} is not a viable input.\n\nPlease Input 0/1\n  0  -  Use a test file\n  1  -  Use your own file\n\nInput:\n")
        
        # Example file Selection
        if test_or_custom == "0":
            print("\nOkay input the file number you want to test!")
            for i in range(len(test_file_names)):
                print(f'  {i}  - "{test_file_names[i]}"')
            chosen_filepath = "../ascii_example_art/" + test_file_names[int(input("\nInput:\n"))] + ".txt"
        
        # Custom file path selection
        elif test_or_custom == "1":
            print("\nOkay lets do this! so First:\nPlease do make sure the file is\n   - in the same directory as this '.py' file\n   - you dont mistype your '.txt' file name!\n\nWhats your file's name?")
            custom_filepath = input("\nInput:\n")
            if ".txt" in custom_filepath:
                chosen_filepath = custom_filepath
            else:
                chosen_filepath = custom_filepath + ".txt"
    
    # Return the chosen file path
    return chosen_filepath, name


# =============================================================================
# Function 2: File Open and File Check Function
#   
#   - Finds and opens file based on File path input
#   - Check File compatability with code and 
#   
# Output:
#   
#   - file contents
#   - file sizing
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
        return file_contents_string, image_width, (image_height * 2)
    
    else:
        print(f"I'm sorry it seems the file you picked is not compatible with this current system version.\nPlease make sure all rows are the same length as the top row which has a length of {image_width} characters.\n\nBe advised your file failed on line(s) {', '.join(non_compatible_rows)}")
        return None, None, None


# =============================================================================
# Function 3: PPM File Header Creator
# 
#   - Creates header string based on opened ascii file
#
# Output:
#   
#   - PPM file Header
# =============================================================================

def create_ppm_header(image_width, image_height):
    
    # PPM type
    header_type = "P3"
    
    # Max RGB color Value
    color_max = 255
    
    return f"{header_type}\n{image_width} {image_height}\n{color_max}\n"


# =============================================================================
# Function 4 & 4.5: Color Selection Functions
# 
#   - Prompt User for Color Selection
#   - Color Sourced from imported Color Data Base
#   
# Output:
#   
#   - Selected RGB Color Code
# =============================================================================

def color_set():
    
    # Declare Variables
    colors_csv_filepath = "../documentation/color_dataset/color_names_kaggle.csv"
    colors = {}
    
    # ** Creating Color Database **
    # Open and read Color CSV
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
            colors[color_name] = [color_r, color_g, color_b]
            
    # Return Color Directory
    return colors
            

def color_selection():  
    
    # Declare Variables
    color_selected = []
    colors = color_set()
          
    # ** Prompting Color Selection **
    # User input
    user_color_selection = input("What color would you like to use today?\n\nInput:\n")
    
    # While Loop Parsing and/ or Confirming Color Selection
    while len(color_selected) < 1:
        if user_color_selection.lower() in colors:
            color_selected = colors[user_color_selection.lower()]
        else:
            print(f"\nIm sorry '{user_color_selection}' is not a color we have listed in our dataset.")
            
            # Search and list potential options
            potentials = []
            page = 1
            check_one = "n"
            
            # Searching and Collating
            for color in colors.keys():
                if user_color_selection in color:
                    potentials.append(color)
            
            if len(potentials) != 0:
                
                # Color Search System:
                while check_one == "n":
                    
                    # Printing potential options by page/ groups of 5
                    print("Could it be any of:")
                    for i in range((page-1)*5, page * 5):
                        print(f"   {i}  - {potentials[i]}")
                    print(f"\npage# ({page}/{(len(potentials)//5)})\n")
                    
                    # Cycle pages
                    if page < (len(potentials)//5):
                        page += 1
                    else:
                        page = 1
                    
                    # Option Selection
                    check_one = input("Do you see the color you wanted above?\n   y  - If yes, Please Input the number listed with the color above\n   n  - For next page, Please input n\n   q  - To quit, Please Input q\n\nInput:\n")
                    
                # Make sure entry is viable 
                if check_one.isdigit():
                    color_selected = colors[potentials[min((int(check_one)), (len(potentials) - 1))]]
                
                else:
                    color_selected.append(None)
                    
            else:
                # Default Last Check
                check_two = input("\nOkay Sorry I guess we really don't have '{user_color_selection}' in our dataset.\nWould you like to retry with another color, input an RGB code directly or Give up?\n\nPlease Input 1 or 2 or 3\n  1  - Retry\n  2  - Input RGB\n  3  - Give Up\n\nInput:\n")
                
                if check_two == "1":
                    user_color_selection = input("\nWhat color would you like to use today?\n\nInput:\n")
                elif check_two == "2":
                    red_code = int(input("\nThe Red decimal code (0 - 255) in the RGB is\n\nInput:\n"))
                    green_code = int(input("\nThe Green decimal code (0 - 255) in the RGB is\n\nInput:\n"))
                    blue_code = int(input("\nThe Blue decimal code (0 - 255) in the RGB is\n\nInput:\n"))
                    color_selected.append(red_code)
                    color_selected.append(green_code)
                    color_selected.append(blue_code)
                else:
                    color_selected.append(None)
       
    # Return Color RGB Selection 
    return(color_selected)


# =============================================================================
# Functions 5: Color Systems
# 
#   - Creates a Dictionare relating the Defined Ascii Character Ramp to RGB color codes
#       - Purpose made functions for each Color System
#
# Output:
#
#   - Mapped Color Dictionary
# =============================================================================

# Global Variable
# Define Base Character Ramp and Length
character_ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
n_steps = len(character_ramp)


# Single Color - Mono Color Swatch Creator
def mono_color_swatch(color_selected):
    
    # Declare Target Variables
    color_range = {}
    mid_point = n_steps//2

    # for loop mapping ascii ramp to color range
    for i in range(n_steps):
        # Even Length Lists
        if n_steps % 2 ==0:
            if i == 0:
                r_code = 0
                g_code = 0
                b_code = 0
            elif i < (mid_point-1):
                r_code += (color_selected[0]) / (mid_point - 1)
                g_code += (color_selected[1]) / (mid_point - 1)
                b_code += (color_selected[2]) / (mid_point - 1)
            elif i in [mid_point-1,mid_point]:
                r_code = color_selected[0]
                g_code = color_selected[1]
                b_code = color_selected[2]
            elif i > (mid_point):
                r_code += (255 - color_selected[0]) / (mid_point)
                g_code += (255 - color_selected[1]) / (mid_point)
                b_code += (255 - color_selected[2]) / (mid_point)
        
        # Odd Length Lists
        else:
            if i == 0:
                r_code = 0
                g_code = 0
                b_code = 0
            elif i < (mid_point):
                r_code += (color_selected[0]) / (mid_point)
                g_code += (color_selected[1]) / (mid_point)
                b_code += (color_selected[2]) / (mid_point)
            elif i == (mid_point):
                r_code = color_selected[0]
                g_code = color_selected[1]
                b_code = color_selected[2]
            elif i > (mid_point):
                r_code += (255 - color_selected[0]) / (mid_point)
                g_code += (255 - color_selected[1]) / (mid_point)
                b_code += (255 - color_selected[2]) / (mid_point)
        
        color_range[character_ramp[i]] = [int(r_code),int(g_code),int(b_code)]
    
    return color_range


# Two Colors - Duo Color Swatch Creator
def duo_color_swatch(color_one, color_two):
    
    # Declare Target Variable
    color_range = {}
    
    # for loop mapping ascii ramp to color range
    for i in range(n_steps):
        if i == 0:
            r_code = color_one[0]
            g_code = color_one[1]
            b_code = color_one[2]
        else:
            r_code += (color_two[0] - color_one[0]) / (n_steps - 1)
            g_code += (color_two[1] - color_one[1]) / (n_steps - 1)
            b_code += (color_two[2] - color_one[2]) / (n_steps - 1)
        
        color_range[character_ramp[i]] = [int(r_code),int(g_code),int(b_code)]
    
    return color_range


# Three Colors - Tri Color Swatch Creator
def tri_color_swatch(color_one, color_two, color_three):
    
    # Declare Target Variable
    color_range = {}
    mid_point = n_steps//2
    
    # For Loop napping ascii ramp to color ranges
    for i in range(n_steps):
        # Even Length Lists
        if n_steps % 2 ==0:
            if i == 0:
                r_code = color_one[0]
                g_code = color_one[1]
                b_code = color_one[2]
            elif i < (mid_point-1):
                r_code += (color_two[0] - color_one[0]) / (mid_point - 1)
                g_code += (color_two[1] - color_one[1]) / (mid_point - 1)
                b_code += (color_two[2] - color_one[2]) / (mid_point - 1)
            elif i in [mid_point-1, mid_point]:
                r_code = color_two[0]
                g_code = color_two[1]
                b_code = color_two[2]
            elif i > (mid_point):
                r_code += (color_three[0] - color_two[0]) / (mid_point - 1)
                g_code += (color_three[1] - color_two[1]) / (mid_point - 1)
                b_code += (color_three[2] - color_two[2]) / (mid_point - 1)
        
        # Odd Length Lists
        else:
            if i == 0:
                r_code = color_one[0]
                g_code = color_one[1]
                b_code = color_one[2]
            elif i < (mid_point):
                r_code += (color_two[0] - color_one[0]) / (mid_point)
                g_code += (color_two[1] - color_one[1]) / (mid_point)
                b_code += (color_two[2] - color_one[2]) / (mid_point)
            elif i == (mid_point):
                r_code = color_two[0]
                g_code = color_two[1]
                b_code = color_two[2]
            elif i > (mid_point):
                r_code += (color_three[0] - color_two[0]) / (mid_point)
                g_code += (color_three[1] - color_two[1]) / (mid_point)
                b_code += (color_three[2] - color_two[2]) / (mid_point)
        
        color_range[character_ramp[i]] = [int(r_code),int(g_code),int(b_code)]
    
    return color_range


# =============================================================================
# Function 6: Color System Selection Function
#
#   - Allows uses to pick and run one of the Above Color Systems
#
# Output
#
#   -  color system specific color range dictionary
# =============================================================================

def pick_color_system():
    
    # Initial Question
    color_system_toggle = input("\nVery Nice!! Which Color system would you like to use?\n\nWe have:\n   0  - Mono Tone Color System\n   1  - Duo Tone Color System\n   2  - Tri Tone Color System\n\nInput:\n")
    
    # Mono Tone System
    if color_system_toggle == "0":
        print("\nGreat, we will need you to pick ONE color!")
        
        # Select Colors
        print("\nPick First Color")
        color_1 = color_selection()
        
        # Run Color System Function
        if color_1 != None:
            return mono_color_swatch(color_1)
        
    # Two Tone System
    if color_system_toggle == "1":
        print("\nGreat, we will need you to pick TWO colors!")
        
        # Select Colors
        print("\nPick First Color  -  SHADOWS")
        color_1 = color_selection()
        
        print("\nPick Second Color  -  HIGHTLIGHTS")
        color_2 = color_selection()
        
        # Run Color System Function
        if color_1 != None or color_2 != None:
            return duo_color_swatch(color_1, color_2)
        
    # Three Tone System
    if color_system_toggle == "2":
        print("\nGreat, we will need you to pick THREE colors!")
        
        # Select Colors
        print("\nPick First Color  -  SHADOWS")
        color_1 = color_selection()
        
        print("\nPick Second Color  -  MIDTONES")
        color_2 = color_selection()
         
        print("\nPick Third Color  -  HIGHLIGHTS")
        color_3 = color_selection()
        
        # Run Color System Function
        if color_1 != None or color_2 != None or color_3 != None:
            return tri_color_swatch(color_1, color_2, color_3)
    
# =============================================================================
# Function 7: PPM String Generator
# 
#   - Maps Colors from designated Color Dictionary to ascii artwork
#
# Output
#
#   - ppm string content
# =============================================================================

def ppm_file_contents(ascii_string, ascii_colors):
    
    # Define Output String
    ppm_output_str = ""
    
    # P3 PPM Row Loop function
    for row in ascii_string.splitlines():
        for i in range(2):          # print each line twice to make up for text height
            for pixel in row:
                if pixel in ascii_colors.keys():
                    ppm_output_str += f"{ascii_colors[pixel][0]} {ascii_colors[pixel][1]} {ascii_colors[pixel][2]} "
            ppm_output_str += "\n"
    
    return ppm_output_str


# =============================================================================
# Function 8: File Naming & Output
#
# Output
#
#   - File Output
# =============================================================================

def output_ppm(name, header, contents, image_height, image_width):
    
    # writing out a file using python I/O
    with open(f"../image_outputs/{name}.ppm", "w") as ppm_file:
        
        ppm_file.write(header)
        
        ppm_file.write(contents)
        print(f"\nAn image has been outputed to /image_outputs:\n\n  File Name: {name}.ppm\n  Image Height: {int(image_height/2)} pixels\n  Image Width: {image_width} pixels\n  Total Pixels: {(image_height/2) * image_width} pixels")


# =============================================================================
# Main Function
# 
#   - Calls all functions above with failsafes and such as tested below
# =============================================================================

def pixelize_ascii():
    
    # Function 1 - Determine File path
    filepath, name = pick_file_path()
    
    if filepath != None:
        try:
            
            # Function 2 - Open and Check File Contents
            file_contents, ascii_width, ascii_height = file_open(filepath)
            
        except FileNotFoundError:
            
            print("\n**Failed** I'm Sorry, the file you requested was not found.\n\nPlease check\n   - the file directory again to make you didnt mistype the filename\n   - the file is in the right location.\nThen run me again!")
        
        else:
            if file_contents!= None:
                
                # Function 3 - Create PPM file header string
                ppm_header = create_ppm_header(ascii_width, ascii_height)
                
                # Function 6 - Color System Selector % Runner
                # Functions 4 - Color Selection & Function 5 - Color Mapper are Called within Function 6
                color_swatch = pick_color_system()
                
                if color_swatch != None:
                    
                    # Function 7 - Transcribe ASCII Art contents into ppm RGB codes
                    ppm_contents = ppm_file_contents(file_contents, color_swatch)
                    
                    # Function 8 - Write and Output PPM File
                    output_ppm(name, ppm_header, ppm_contents, ascii_height, ascii_width)


# =============================================================================
# RUN FUNCTION
# =============================================================================

pixelize_ascii()