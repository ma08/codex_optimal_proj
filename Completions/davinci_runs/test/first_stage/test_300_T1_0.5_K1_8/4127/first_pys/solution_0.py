

import sys

def main():
    """Main function"""
    a = int(sys.stdin.readline().strip().split()[0])
    b = float(sys.stdin.readline().strip())
    print(int(a*b))

if __name__ == '__main__':
    main()