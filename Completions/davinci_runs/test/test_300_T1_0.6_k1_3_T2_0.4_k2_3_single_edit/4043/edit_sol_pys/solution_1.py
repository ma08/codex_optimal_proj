import os
import sys
import shutil

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isdir(path):
            dir_list = os.listdir(path)
            for file in dir_list:
                if os.path.isfile(file):
                    print(file)
        else:
            print("Not a directory")
    else:
        print("No path specified")

if __name__ == "__main__":
    main()
