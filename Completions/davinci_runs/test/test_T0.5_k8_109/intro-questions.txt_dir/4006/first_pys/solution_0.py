

# Solution

import sys

def main():
    n = int(input())
    for i in range(1,n+1):
        if(i<10):
            print(10-i)
        else:
            print(19)
            break

if __name__ == "__main__":
    main()