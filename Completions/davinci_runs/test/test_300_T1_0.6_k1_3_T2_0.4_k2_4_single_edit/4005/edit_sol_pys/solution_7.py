import os
import sys

def main():
    print("Current working directory: ", os.getcwd())
    print("Command line arguments: ", sys.argv)

if __name__ == "__main__":
    main()
