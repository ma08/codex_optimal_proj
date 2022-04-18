

import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    for i in range(len(a)):
        if a[i] in b:
            print(a[:i] + a[i].upper() + a[i+1:])
            break            

if __name__ == "__main__":
    main()
