import os
import sys

def main(argv):
    if len(argv) != 2:
        print('Usage: python file.py [filename]')
        sys.exit(1)

    filename = argv[1]
    if not os.path.exists(filename):
        print('Error: file %s does not exist' % filename)
        sys.exit(1)

    if os.path.isdir(filename):
        print('Error: %s is a directory' % filename)
        sys.exit(1)

    print(file_type(filename))

def file_type(filename):
    with open(filename, 'rb') as f:
        file_start = f.read(32)
        file_type = None
        for file_sig in file_signatures:
            if file_start.startswith(file_sig[1]):
                file_type = file_sig[0]
                break
        if file_type is not None:
            return file_type
        else:
            return 'Unknown'

file_signatures = [
    ('JPEG', b'\xff\xd8\xff'),
    ('PNG', b'\x89PNG\r\n\x1a\n'),
    ('GIF', b'GIF87a')
]

if __name__ == '__main__':
    main(sys.argv)
