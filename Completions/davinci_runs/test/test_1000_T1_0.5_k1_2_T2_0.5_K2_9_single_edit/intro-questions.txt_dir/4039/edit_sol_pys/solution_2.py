
import os
import glob

def main():
    print(os.path.isfile('file.py'))
    print(os.path.isdir('file.py'))
    print(os.path.isfile('/tmp'))
    print(os.path.isdir('/tmp'))

    print(glob.glob('*.py'))

if __name__ == "__main__":
    main()
