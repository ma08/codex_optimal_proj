
import sys

def main():
    f = open(sys.argv[1])
    for line in f:
        print line

if __name__ == "__main__":
    main()
