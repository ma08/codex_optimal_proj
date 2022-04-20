import os
import sys

def main():
    if len(sys.argv) == 1:
        print('No directory specified.')
        sys.exit()
    else:
        dirname = sys.argv[1]
        if not os.path.isdir(dirname):
            print('Directory does not exist.')
            sys.exit()
        else:
            for filename in os.listdir(dirname):
                print(filename)

if __name__ == '__main__':
    main()
