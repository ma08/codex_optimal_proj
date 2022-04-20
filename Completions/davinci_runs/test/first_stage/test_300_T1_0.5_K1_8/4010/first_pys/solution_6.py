

import sys

def read_ints():
    return list(map(int, input().split()))

def read_int():
    return int(input())

def main():
    t = read_int()
    for _ in range(t):
        n = read_int()
        a = read_ints()
        for i in range(n):
            for j in range(i+1, n):
                if a[i] == a[j]:
                    for k in range(j+1, n):
                        if a[i] == a[k]:
                            print("YES")
                            break
                    else:
                        print("NO")
                    break
            else:
                continue
            break
        else:
            print("NO")

if __name__ == "__main__":
    main()