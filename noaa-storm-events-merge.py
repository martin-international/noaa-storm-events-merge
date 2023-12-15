import os
import concurrent.futures
import tkinter as tk
from tkinter import filedialog
import csv
import logging

class NOAAStormEventsParser:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_file = os.path.join(output_folder, 'merged_data.csv')

    def parse_line(self, line):
        return line.strip().split('|')

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as file:  # Handle BOM with utf-8-sig
            with open(self.output_file, 'a', newline='', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                for line in file:
                    parsed_data = self.parse_line(line)
                    csv_writer.writerow(parsed_data)

    def process_storm_events_files(self):
        file_paths = [os.path.join(self.input_folder, f) for f in os.listdir(self.input_folder)]
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(self.process_file, file_path) for file_path in file_paths]
            concurrent.futures.wait(futures)
        logging.info("NOAA Storm Events data processing completed.")

def select_directory(title):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()
    return folder_path

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    input_folder = select_directory("Select the Input Folder")
    output_folder = select_directory("Select the Output Folder")

    if input_folder and output_folder:
        parser = NOAAStormEventsParser(input_folder, output_folder)
        parser.process_storm_events_files()
    else:
        logging.info("Input folder or output folder not selected. Exiting.")

if __name__ == '__main__':
    main()
