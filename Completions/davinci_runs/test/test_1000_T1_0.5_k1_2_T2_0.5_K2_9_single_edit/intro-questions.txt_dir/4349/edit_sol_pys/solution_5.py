#!/usr/bin/python

import os

def main():
    f = open("test.txt", "w")
    f.write("Hello World\n")
    f.write("This is our new text file\n")
    f.write("and this is another line.\n")
    f.write("Why? Because we can.\n")
    f.close()

if __name__ == "__main__":
    main()
