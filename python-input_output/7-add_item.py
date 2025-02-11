#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    # Check if there are command-line arguments (excluding the script name)
    arguments = sys.argv[1:]

    # Try to load existing data from the file, if it exists
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []  # If the file doesn't exist, initialize an empty list

    # Add the command-line arguments to the list
    items.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(items, 'add_item.json')

if __name__ == "__main__":
    main()

