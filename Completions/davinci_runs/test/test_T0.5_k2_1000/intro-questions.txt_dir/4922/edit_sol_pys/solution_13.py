

import sys

def main(filepath):
    with open(filepath, 'r') as f:
        m, n = [int(i) for i in f.readline().strip().split()] # m is the number of hours, n is the number of days.
        
        if m < 8:
            print('unsatisfactory')
        else:
            print('satisfactory')

if __name__ == '__main__':
    main(sys.argv[1])
