import sys

def main():
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "<filename>")
        exit(1)
    filename = sys.argv[1]
    print("File name:", filename)

if __name__ == '__main__':
    main()
