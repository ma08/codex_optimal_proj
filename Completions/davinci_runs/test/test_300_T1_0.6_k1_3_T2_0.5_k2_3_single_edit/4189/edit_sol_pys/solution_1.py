import os
import sys

def main():
    path = sys.argv[1]
    if os.path.isdir(path):
        for item in os.listdir(path):
            print(item)
    else:
        print('Not a directory')

if __name__ == '__main__':
    main()
