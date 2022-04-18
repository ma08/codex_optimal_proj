
import sys

def main():
    line1 = [int(x) for x in sys.stdin.readline().split()]
    line2 = [int(x) for x in sys.stdin.readline().split()]
    line1.sort()
    line2.sort()
    diff = line1[1] - line2[0]
    print(line1[2] + diff)

if __name__ == '__main__':
    main()
