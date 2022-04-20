import os
import sys
import shutil

def main():
    try:
        file_name = sys.argv[1]
        if os.path.exists(file_name):
            os.remove(file_name)
            print("File removed")
        else:
            print("File does not exist")
    except IndexError:
        print("Please provide a file name")

if __name__ == '__main__':
    main()
