#!/usr/bin/env python3

import os
import argparse
from utils import _create_folder_and_file


if __name__ == "__main__":
    # Parse arguments:
    parser = argparse.ArgumentParser(description="Advent of Code 2023")
    parser.add_argument("day", type=int, help="The day to run.")
    args = parser.parse_args()

    if args.day < 1 or args.day > 25:
        print("Day must be between 1 and 25.")
        exit(1)
    
    # Create folder and file if they don't exist:
    if not _create_folder_and_file(args.day):
        # If the folder and file already exist, run the main.py file:
        os.system(f"python3 {args.day}/main.py")
