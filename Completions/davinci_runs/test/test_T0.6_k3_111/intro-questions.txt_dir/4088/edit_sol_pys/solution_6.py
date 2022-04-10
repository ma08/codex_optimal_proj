#!/usr/bin/python3

import os

def main():
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir('/home/student/mycode/'))
    print(os.listdir('/home/student/mycode/')) 

if __name__ == "__main__":
    main()
