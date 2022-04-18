
import sys

def main():
    year = int(sys.stdin.readline())
    if year % 26 == 2 or year % 26 == 8 or year % 26 == 14 or year % 26 == 20: 
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
