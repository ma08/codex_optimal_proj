
# Solution

#!/usr/bin/python3

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if a[0] == a[n-1]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
