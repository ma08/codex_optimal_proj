import os
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Please enter a file name")
        return
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("File does not exist")
        return
    print("File exists")
    print("File size: ", os.path.getsize(filename))
    print("File created: ", time.ctime(os.path.getctime(filename)))
    print("File modified: ", time.ctime(os.path.getmtime(filename)))
    print("File accessed: ", time.ctime(os.path.getatime(filename)))

if __name__ == "__main__":
    main()
