

#!/usr/bin/env python

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print("YES" if list(map(int, input().split()))[0] == list(map(int, input().split()))[-1] else "NO")

if __name__ == "__main__":
    main()
