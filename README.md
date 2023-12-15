# NOAA Storm Events Merging Script

## Overview
The NOAA Storm Events Merging Script is a Python-based tool that efficiently merges multiple pipe-separated (`|`) text files containing storm event data into a single CSV file. This tool is especially useful for consolidating large NOAA datasets, facilitating easier data analysis and visualization. The script employs parallel processing and a graphical interface for ease of use.

## Features
- **Efficient Line-by-Line Processing**: Reads files line by line, ensuring low memory usage even with large files.
- **Concurrent Processing**: Utilizes Python's concurrent futures to process multiple files in parallel, significantly improving performance.
- **Graphical File Selection**: Uses Tkinter-based dialogs for easy selection of input and output directories.
- **UTF-8 Encoding Support**: Handles UTF-8 Byte Order Mark (BOM) to ensure correct text interpretation.
- **Streaming Data Writing**: Directly writes processed data to a CSV file in a streaming manner, reducing memory and I/O overhead.

## Requirements
- Python 3.x
- Concurrent Futures (part of the standard library in Python 3.x)
- Tkinter (usually comes pre-installed with Python)

## Usage

### Running the Script
1. **Execute the Script**: Run `noaa-storm-events-merge.py` in your Python environment. The script will prompt you to select the input folder and output folder.
2. **Input Folder**: Choose the folder containing the pipe-separated (`|`) text files for merging.
3. **Output Folder**: Select the folder where the merged CSV file will be saved.

### Customization
- **File Parsing**: Modify the `parse_line` method in the `NOAAStormEventsParser` class to adapt to different file formats or delimiters.
- **File Format**: The script currently handles pipe-separated text files. Adjustments can be made for other delimiters or file structures.

## Limitations
- The script is optimized for pipe-separated files without header rows. For files with different formats or complex structures, the parsing logic will need customization.

## Additional Information
- Ensure that Python and Tkinter are correctly installed on your system before running the script.
- The script is designed to be user-friendly and suitable for processing extensive NOAA storm data files.
