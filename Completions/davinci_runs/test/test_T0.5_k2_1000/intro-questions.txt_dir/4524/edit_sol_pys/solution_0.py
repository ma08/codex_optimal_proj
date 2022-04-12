#!/usr/bin/env python3

import os

def main():
    print(os.getcwd())
    os.chdir('/home/student/mycode/')
    print(os.getcwd())
    print(os.listdir('.'))

if __name__ == "__main__":
    main()
