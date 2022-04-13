

import sys

def main(filepath):
    try:
        with open(filepath, 'r') as f:
            m, n = [int(i) for i in f.readline().strip().split()] # read the first line and split it into two integers
            
            if m < 8:
                print('unsatisfactory')
            else:
                print('satisfactory')
    except TypeError:
        print('Error: filepath is not a string')
    except FileNotFoundError:
        print('Error: file not found')

if __name__ == '__main__':
    main(sys.argv[1])
