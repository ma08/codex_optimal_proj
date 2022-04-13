import sys
import os


def get_file_info(file_path):
    #get the file path
    #get the size of the file in bytes
    #get the last modified date
    #return the size and date
    size = os.path.getsize(file_path)
    date = os.path.getmtime(file_path)
    return [size, date]

def main(file_path):
    #get the file path and print the size and date of the file
    info = get_file_info(file_path)
    print('Size: {} bytes'.format(info[0]))
    print('Last modified: {}'.format(info[1]))


if __name__ == '__main__':
    main(sys.argv[1])
