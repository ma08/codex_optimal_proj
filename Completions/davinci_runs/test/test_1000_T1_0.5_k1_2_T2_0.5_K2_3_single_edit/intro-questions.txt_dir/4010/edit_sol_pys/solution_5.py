
# Solution

#!/bin/python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] == a[-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
