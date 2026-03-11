# ASCII Tonal Image Generator

## Problem Being Solved

ASCII art was one of the earliest widely accessible forms of digitally created art known to man. Using only keyboard characters, artists and everyone at home were able to simulate light, shadows, and textures to form digital artworks long before modern image editing tools were available. It was a creative medium which was created and popularized through the curiosity of users into early accessible tech and despite of the technical constraints and limitations, and has led to expressive, inventive, and unique computational art still made today.

Over time, however, ASCII art has increasingly become overlooked and largely forgotten by younger generations. Its monochrome, character-based structure limits it to basic tonal variations and prevents it from representing color and intensity in the way modern digital images do. Additionally as ASCII art exists purely as structured textfiles rather than pixel-based image data, it also cannot easily be integrated with the various popularized modern image workflows that allow everyday users to edit, play around with, or share and post content through social media using standard graphics tools and applications as most platforms would fail simply due to character width limitations. As a result, ASCII artworks are often confined to static text files and the forums dedicated to them in which their creativity can be explored and must be viewed in specific formats, making them less accessible and interactive compared to almost every other digital artistic medium.

This project addresses that limitation by defining and implementing a deterministic system that can translate ASCII character-based tonal density into scaled RGB pixel data which will be easier for users to consume. The program reads an ASCII text file, interprets each character according to a predefined tonal ranking system, applies scaled variations of a user-selected base color, and generates a valid PPM raster image file.

In doing so, this project bridges symbolic text-based visual encoding and structured pixel-based image representation using only fundamental Python constructs.

---

## Project Overview

The ASCII Tonal Image Generator is a Python program created for the University Course CPS109 Project.

The program:

- Reads an ASCII art `.txt` file
- Determines its structural dimensions (height and width)
- Interprets each character as a tonal density level
- Applies a scaled RGB variation of a user-selected base color
- Outputs a valid `.ppm` image file

The output image visually reconstructs the ASCII tonal structure in color form.

---

## How the Program Works

1. **ASCII File Input**
   - The program reads a `.txt` file from the `ascii_example_art/` directory.
   - Each line is stored and parsed to determine image height and width.

2. **Tonal Density Interpretation**
   - Characters are ranked according to a predefined ASCII density ramp.
   - Each character is mapped to a relative brightness level.

3. **User Color Selection**
   - The user selects a base color using:
     - A predefined dictionary of basic colors, or
     - Manual RGB input.
   - A `while` loop ensures valid input.

4. **Color Scaling**
   - The base RGB color is scaled according to tonal depth.
   - Arithmetic expressions compute proportional intensity.

5. **PPM File Generation**
   - A valid P3-format PPM header is constructed.
   - Pixel data is written line-by-line.
   - The final file is saved to `image_outputs/`.

---

## Project Structure

```text
ascii_tonal_image_generator/
│
├── ascii_example_art/
│   ├── ascii-art-smallbanana.txt
│   └── ascii-art-treefrog.txt
│
├── image_outputs/
│   └── temp_output.ppm
│
├── scripts/
│   └── ascii_tonal_image_generation_script.py
│
├── documentation/
│   ├── cps109_project_outline.pdf
│   ├── practice_and_testing/
│   │   ├── ppm_creation_playground.py
│   │   └── color_selection_and_tonal_range_trial.py
│   ├── color_dataset/
│   │   └── color_names_kaggle.csv
│   └── ppm_examples_foundonweb/
│       └── simple.ppm
│
├── .gitignore
└── README.md
```

---

## Key Scripts (Current)

### `ascii_tonal_image_generation_script.py`
Main program that:
- Reads ASCII art
- Maps tonal density
- Applies RGB scaling
- Writes PPM output

### `ppm_creation_playground.py`
Early development script used to:
- Understand PPM file structure
- Experiment with header construction
- Test gradient generation logic

### `color_selection_and_tonal_range_trial.py`
Development script used to:
- Implement color selection logic
- Validate RGB input handling
- Explore tonal variation scaling

---

## Technical Features Demonstrated (CPS109 Requirements)

This project demonstrates all required Python constructs:

- **Variable declarations and assignments**
- **Arithmetic expressions** (RGB scaling calculations)
- **if / elif / else conditionals**
- **Sequence types** (strings, lists, tuples)
- **Nested for loops** (ASCII parsing and pixel generation)
- **While loop** (input validation and selection control)
- **User-defined functions**
- **Print statements for program interaction**
- **File input** (reading ASCII `.txt`)
- **File output** (writing `.ppm` image)

The final program solves the defined problem by deterministically converting symbolic ASCII tonal data into structured RGB pixel output.

---

## Development Notes

This project evolved from an initial exploration of simple ASCII parsing into a more structured system including:

- Modular PPM header construction
- Structured color selection logic
- Tonal depth scaling
- Dedicated experimentation scripts

All development remained within the scope of fundamental Python constructs as required for CPS109.

---

## Output Format

The program generates images in **PPM (P3)** format.

PPM was chosen because:
- It requires no external libraries
- It can be written using plain text file output
- It clearly demonstrates understanding of structured file formatting

Generated images can be viewed using image viewers that support `.ppm` files.

---

## Future Extensions (Optional)

Potential expansions include:

- Dynamic tonal ramp detection
- Automatic character density ranking
- PNG output using external libraries
- GUI-based color selection

These features were intentionally excluded to maintain assignment scope and focus on core Python constructs.

---

## Author

Sean Schallberger  
CPS109 Toroto Metropolitan University
2026
