
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    for i in range(m):
        if a[i] > b[i]:
            print("NO")
            return
        if a[i] + c[i] < b[i]:
            print("NO")
            return


    print("YES")

if __name__ == '__main__':
    main()
