import sys

def main():
    f = open(sys.argv[1],'r')
    for line in f:
        print line
    f.close()

if __name__ == '__main__':
    main()
