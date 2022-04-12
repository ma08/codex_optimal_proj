import os
import glob

def main():
    os.chdir('./')
    for file in glob.glob('*.txt'):
        print(file)
    return

if __name__ == '__main__':
    main()
