import sys

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    for i in range(n-1):
        if l[i] == l[i+1]:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    main()
