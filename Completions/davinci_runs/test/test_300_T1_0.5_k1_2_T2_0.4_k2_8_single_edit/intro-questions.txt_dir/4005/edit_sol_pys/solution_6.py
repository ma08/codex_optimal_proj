import os
import sys

def main():
    # get the directory name from the command line
    try:
        directory = sys.argv[1]
    except IndexError:
        print("Usage: file.py <directory>")
        sys.exit(1)

    # get the file names from the directory
    file_names = os.listdir(directory)

    # process the files
    for file_name in file_names:
        full_file_name = os.path.join(directory, file_name)
        if os.path.isfile(full_file_name):
            process_file(full_file_name)

def process_file(file_name):
    print("Processing:", file_name)

if __name__ == "__main__":
    main()
