
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(n): 
        if a[i] == 1:
            a_count += 1
        if b[i] == 1:
            b_count += 1
        if c[i] == 1:
            c_count += 1
    print(a_count)
    print(b_count)
    print(c_count)

if __name__ == '__main__':
    main()
