
import sys

def main():
    line = sys.stdin.readline().strip()
    s1, s2, s3, s4 = [int(x) for x in line.split()]
    s = s1 + s2 + s3 + s4
    print(s*(s-2*s1)*(s-2*s2)*(s-2*s3)*(s-2*s4)**(-0.5))

if __name__ == '__main__':
    main()
