
import os, sys

def main():
    if len(sys.argv) == 1:
        print("Error: No file specified")
        return
    if not os.path.isfile(sys.argv[1]):
        print("Error: File not found")
        return
    file = open(sys.argv[1], 'r')
    print(file.read())
    file.close()

if __name__ == '__main__':
    main()
