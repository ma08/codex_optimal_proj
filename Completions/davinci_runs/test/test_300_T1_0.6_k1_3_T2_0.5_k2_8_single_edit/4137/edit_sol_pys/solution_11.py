
import os
import sys
import json
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file.py [filepath] [name]")
        sys.exit(1)
    file_path = sys.argv[1]
    name = sys.argv[2]
    if not os.path.exists(file_path):
        print("File does not exist")
        sys.exit(1)
    if not os.path.isfile(file_path):
        print("Please specify a file")
        sys.exit(1)
