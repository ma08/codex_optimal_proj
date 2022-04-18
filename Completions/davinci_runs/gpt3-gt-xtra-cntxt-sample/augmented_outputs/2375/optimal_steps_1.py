import sys

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(solve(n, a))

def solve(n, a):
    a.sort()
    currNum = a[0]
    currCount = 0
    ans = 0
    for i in range(n):
        if a[i] == currNum:
            currCount += 1
        else:
            if currCount > 2:
                ans += currCount
            elif currCount == 2:
                ans += currCount - 1
            currNum = a[i]
            currCount = 1
    if currCount > 2:
        ans += currCount
    elif currCount == 2:
        ans += currCount - 1
    return ans


if __name__ == "__main__":
    main()