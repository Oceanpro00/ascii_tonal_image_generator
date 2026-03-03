# ASCII Tonal Image Generator

## Project Overview

The **ASCII Tonal Image Generator** is a self-led and proposed Python program for my course CPS109 that aims to convert online generated ASCII art text files into colored tonal images based on user-based color selection.

Using the fact that each ASCII character represents a different level of visual tonal density (dark to light), the program will attempt to map those characters into scaled variations of the pixel colors, making use of a user-prompted base RGB color selection to generate different tonal ranges of each of the color pixels, resulting in a pixel-based color image as output.

---

## Version 1 Scope

This initial version will be designed to work with ASCII art generated using:

https://vaultandzn.com/pages/ascii-art-generator/

This is due to the fact that the program will initially assumes a fixed "agreed upon" tonal character scale in order to effectively and correctly create the pixel art.  
Future versions will aim to support automatic dynamic reading of the ascii characters used to create an appropriate tonal range.

---

## How it will work

1. The program reads a generated ASCII `.txt` file
2. Each character is read and matched to a brightness level using a predefined tonal scale
3. The user selects a base RGB color
4. The program scales that color onto a tonal range based on character brightness
5. A `.ppm` image file is generated and output using computed RGB values

---

## Example ASCII Input

```
@@@@@@
@@..@@
@....@
@@..@@
@@@@@@
```

Each character corresponds to a tonal value as depicted by their density.  
Denser characters produce/ represent darker color variations.

---

## Output

The program will generate a Portable Pixel map `.ppm` image file that can be opened in most standard image viewers as an image file.

Each ASCII character will represent and become a colored pixel block in the final outputted image.
