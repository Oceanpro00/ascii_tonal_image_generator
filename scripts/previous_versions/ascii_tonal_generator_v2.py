#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:13:02 2026

Project: ascii_tonal_generator

Prime Targets:
    - Clean up v1 Function logic
        - Split each logi part of the function into seperate functions
        - Have 1 function call all other functions thus giving us cleaner code
    - Add other color ways (Will be done in v3)

@author: seanschallberger
"""

# =============================================================================
# Function 1: Welcome Sequence 1:
#   
#   - Pick and design ascii art filepath
#       - Pick either an example Test file or user's own file
# =============================================================================

def pick_file_path():
    
    # Define Function 1 Variables
    test_file_names = ["ascii-art-treefrog", "ascii-art-sunset", "ascii-art-chameleon", "ascii-art-geometric-circle", "ascii-art-marilyn"]
    chosen_filepath = ""
    
    # Start Up Statement
    run_check = input("Hello User!\n\nDo you want to try generating an Ascii Tonal Artwork?\n  y  - yes\n  n  - no\n\nInput:\n")
    
    # File Name/ Path defining    -->  Returns file filepath from here
    if run_check.lower() == "n":
        print("\nOkay! Till next time!")
        return None, None
    else:
        name = input("\nThats awesome! What would you like to name the file?\n\nInput:\n")
        test_or_custom = input("\nIncredible name! do you want to generate one using one of the example test files or your own ascii art file??\n\nPlease Input 0/1\n  0  -  Use a test file\n  1  -  Use your own file\n\nInput:\n")
        
        # Ensure Correct Input
        while test_or_custom not in ["0","1"]:
                test_or_custom = input(f"\n{test_or_custom} is not a viable input.\n\nPlease Input 0/1\n  0  -  Use a test file\n  1  -  Use your own file\n\nInput:\n")
        
        if test_or_custom == "0":
            print("\nOkay input the file number you want to test!")
            for i in range(len(test_file_names)):
                print(f'  {i}  - "{test_file_names[i]}"')
            chosen_filepath = "../ascii_example_art/" + test_file_names[int(input("\nInput:\n"))] + ".txt"
        
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
        return file_contents_string, image_width, (image_height * 2)
    
    else:
        print(f"I'm sorry it seems the file you picked is not compatible with this current system version.\nPlease make sure all rows are the same length as the top row which has a length of {image_width} characters.\n\nBe advised your file failed on line(s) {', '.join(non_compatible_rows)}")
        return None, None, None


# =============================================================================
# Function 3: PPM File Header Creator
# 
#   - Creates header string based on opened ascii file
# =============================================================================

def create_ppm_header(image_width, image_height):
    
    # PPM type
    header_type = "P3"
    
    # Max RGB color Value
    color_max = 255
    
    return f"{header_type}\n{image_width} {image_height}\n{color_max}\n"
    

# =============================================================================
# Function 4 & 4.5: Color Selection Function
# 
#   - Input and If Statement Loop to prompt user to select color
#       - Allow user to confirm and pick proper color names
#   - Color name input is converted to a RGB code
#       - Import color list from csv file sourced from kaggle
#
#   - v2 improvements:
#       - allow code to function/ make sense even if called up multiple times
#       - check user color selection when color name not found and offer up alternative colors
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
    user_color_selection = input("\nWhat color would you like to use today?\n\nInput:\n")
    
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
                while check_one == "n":
                    
                    # Printing by page
                    print("Could it be any of:")
                    for i in range((page-1)*5, page * 5):
                        print(f"   {i}  - {potentials[i]}")
                    print(f"\npage# ({page}/{(len(potentials)//5)})\n")
                    
                    # Cycle pages
                    if page < (len(potentials)//5):
                        page += 1
                    else:
                        page = 1
                    
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
# Function 5: Ascii Ramp --> Color Swatch Generator
# 
#   - Creates a Dictionare relating the Defined Ascii Character Ramp to RGB color codes
#       - v1 currently only does black -> selected color -> white  (COMPLETE)
#       - v2 is hoped to have multiple methods  (PROPOSED)
# =============================================================================

def ascii_color_swatch(color_selected):
    
    # Define Base Character Ramp
    character_ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    # Declare Variables
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
                r_code += (color_selected[0]) / (n_steps/2 - 1)
                g_code += (color_selected[1]) / (n_steps/2 - 1)
                b_code += (color_selected[2]) / (n_steps/2 - 1)
            elif i >= (n_steps/2):
                r_code += (255 - color_selected[0]) / (n_steps/2)
                g_code += (255 - color_selected[1]) / (n_steps/2)
                b_code += (255 - color_selected[2]) / (n_steps/2)
            else:
                r_code = color_selected[0]
                g_code = color_selected[1]
                b_code = color_selected[2]
        else:
            if i == 0:
                r_code = 0
                g_code = 0
                b_code = 0
            elif i < (n_steps/2):
                r_code += (color_selected[0]) / (n_steps/2)
                g_code += (color_selected[1]) / (n_steps/2)
                b_code += (color_selected[2]) / (n_steps/2)
            elif i >= (n_steps/2):
                r_code += (255 - color_selected[0]) / (n_steps/2)
                g_code += (255 - color_selected[1]) / (n_steps/2)
                b_code += (255 - color_selected[2]) / (n_steps/2)
            else:
                r_code = color_selected[0]
                g_code = color_selected[1]
                b_code = color_selected[2]
        
        color_range[character_ramp[i]] = [int(r_code),int(g_code),int(b_code)]
    
    return color_range


# =============================================================================
# Function 6: PPM String Generator
# 
#   - Ascii art string contents --> PPM file content structure
#       - Takes each ascii character and maps the corresponding RGB color code as a pixel
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
# Function 7: File Naming & Output
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
                
                # Function 4 - User Color Selection Tool
                selected_rgb = color_selection()
                
                if selected_rgb[0] != None:
                    
                    # Function 5 - Map Color RGB codes to Ascii Characters based on Density
                    color_swatch = ascii_color_swatch(selected_rgb)
                    
                    # Function 6 - Transcribe ASCII Art contents into ppm RGB codes
                    ppm_contents = ppm_file_contents(file_contents, color_swatch)
                    
                    # Function 7 - Write and Output PPM File
                    output_ppm(name, ppm_header, ppm_contents, ascii_height, ascii_width)


# =============================================================================
# RUN FUNCTION
# =============================================================================

pixelize_ascii()



# =============================================================================
# Function Test Section (Temp)
# 
# **EDITS**
#   - Realized that ill need failsafes between the functions otherwise whole program can fail  
#       - Fail safes using if statements work but require None type returns and can still give certain errors
#       - Try and Except may be best used around certain sections for certain error types
# =============================================================================

"""
# Test Function 1 - Returns Filepath 
test_filepath, test_name = pick_file_path()

if test_filepath != None:
    
    # Test print 1
    # print("\n" + test_filepath)
    
    # Try to find the file with a failsafe through try, except and else
    try:
        
        # Test Function 2 - Returns file contents
        test_file_contents, test_ascii_width, test_ascii_height = file_open(test_filepath)
        
    except FileNotFoundError:
        print("\n**Failed** I'm Sorry, the file you requested was not found.\n\nPlease check\n   - the file directory again to make you didnt mistype the filename\n   - the file is in the right location.\nThen run me again!")
    
    else:
        if test_file_contents != None:
            
            # Test print 2
            # print("\n" + test_file_contents)
    
            # Test Function 3 - Returns file PPM Header
            test_ppm_header = create_ppm_header(test_ascii_width, test_ascii_height)
            
            # Test print 3
            # print(test_ppm_header)
            
            # Test Function 4 - Returns Selected color RGB list
            test_selected_rgb = color_selections()
            
            # Test print 4
            # print(test_selected_rgb)
            
            if test_selected_rgb[0] != None:
                
                # Test Function 5 - Returns Color Swatch Diction Corresponding to Ascii Density
                test_color_swatch = ascii_color_swatch(test_selected_rgb)
                
                # Test print 5
                # print(test_color_swatch)
                
                # Test Function 6  - Returns the ascii art file converted into ppm structured RGB codes that represent pixels
                test_ppm_contents = ppm_file_contents(test_file_contents, test_color_swatch)
                
                # Test print 6
                # print(test_ppm_contents)
                
                # Test Function 7 - Output ppm File 
                output_ppm(test_name, test_ppm_header, test_ppm_contents, test_ascii_height, test_ascii_width)

"""