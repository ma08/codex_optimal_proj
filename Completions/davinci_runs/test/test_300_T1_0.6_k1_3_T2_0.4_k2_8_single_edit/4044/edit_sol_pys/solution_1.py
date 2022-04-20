
#!/usr/bin/env python

if __name__ == '__main__':
    n, m, k = map(int, raw_input().split())
    lst = [int(x) for x in raw_input().split()]
    c = 0
    for i in range(n):
        if (lst[i] == 1):
            c += 1
    print c
