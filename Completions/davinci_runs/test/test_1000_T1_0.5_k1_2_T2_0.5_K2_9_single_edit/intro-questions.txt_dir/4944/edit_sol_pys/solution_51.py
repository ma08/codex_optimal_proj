
import sys

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if i == 0:
            if a[i] == 1:
                count += 1
        elif i == n - 1:
            if a[i] == 1 and a[i - 1] == 1:
                count += 1
        else:
            if a[i] == 1 and a[i - 1] == 1:
                count += 1
            if a[i] == 1 and a[i + 1] == 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
