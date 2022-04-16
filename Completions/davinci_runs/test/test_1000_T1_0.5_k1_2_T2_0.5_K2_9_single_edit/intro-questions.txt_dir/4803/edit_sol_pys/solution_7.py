
import os
import sys
 
def main():
 
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                print(line, end='')
    else:
        print('file not found:', file_name)
 
if __name__ == '__main__':
    main()
