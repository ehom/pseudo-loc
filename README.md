# pseudo_loc 

You can use this command line tool to help you identify concatenated messages and 
check if your visual layouts are localization-friendly.

Conventional Pseudo-localization contains 3 steps:

Step 1: **Character Substitution** &mdash; (eg, swapping unaccented for accented characters)

Step 2: **Text Padding** &mdash; (adding extra chars to the beginning and/or end of each message 
to simulate the lengthiness of localized text)

Step 3: **Bracketing** &mdash; adding a character to the beginning and end of each message resource

This tool only supports Steps 2 and 3.

`Step 3` is enabled by default while `Step 2` needs to be turned on by specifying the option at the command line.

## Overview

![overview](images/pseudo_loc_diagram.svg)

## Command Line Usage

% `pseudo-loc\bin\pseudo_loc -h`

``` 
usage: pseudo_loc [-h] [-p] [-o OUTPUT_FOLDER] [-e EXCLUSION_LIST] [-v] files [files ...]

Pseudo-localize a list of files

positional arguments:
  files                 list of files to be pseudo-localized

optional arguments:
  -h, --help            show this help message and exit
  -p, --pad             add padding to pseudo-localized text
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        folder where the pseudo-localized files will be written to.
  -e EXCLUSION_LIST, --exclusion_list EXCLUSION_LIST
                        name of file containing identifiers of messages that WILL NOT be pseudo-localized
  -v, --version         show program's version number and exit

Thanks for using pseudo_loc!

```