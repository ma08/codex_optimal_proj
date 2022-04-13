import sys

def main():
    for i in range(0, int(sys.stdin.readline())):
        line = sys.stdin.readline().strip()
        if len(line) <= 2 or len(set(line)) <= 2:
            print "0"
        else: print len(line) - 2

if __name__ == '__main__':
    main()
