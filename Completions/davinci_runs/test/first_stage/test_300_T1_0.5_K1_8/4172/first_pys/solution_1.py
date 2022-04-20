

import sys

def main():
    line = input()
    n, k = map(int, line.split())
    line = input()
    a = list(map(int, line.split()))
    a = sorted(a)
    
    if a[0] == a[-1]:
        print(0)
        return
    
    i = 0
    j = n - 1
    count = 0
    while True:
        if a[i] == a[j]:
            break
        if i == j:
            count += 1
            a[i] += 1
        else:
            count += 2
            a[i] += 1
            a[j] -= 1
        i += 1
        j -= 1
        a = sorted(a)
    
    print(count)
    
if __name__ == "__main__":
    main()