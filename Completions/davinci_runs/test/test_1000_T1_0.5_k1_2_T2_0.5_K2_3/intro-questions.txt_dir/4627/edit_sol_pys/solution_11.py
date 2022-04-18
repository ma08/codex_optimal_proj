#
import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        if n == 2:
            if a[0] == a[1] or abs(a[0]-a[1]) == 1:
                print("YES")
            else:
                print("NO")
        else:
            for j in range(0, n-1, 2):
                if a[j] != a[j+1] and abs(a[j]-a[j+1]) != 1:
                    print("NO")
                    break
            else:
                print("YES")

if __name__ == "__main__":
    main()
