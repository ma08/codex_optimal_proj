
from collections import Counter

def main():
    N = int(input())
    d = [int(i) for i in input().split()] # list
    # print(N,d)

    c = Counter(d) # dict
    # print(c)

    d_u = list(set(d))
    d_u.sort()
    # print(d_u)

    s = 0
    for i in d_u:
        s += c[i]*(N-c[i])
    # print(s)

    print(s//2)

if __name__ == '__main__':
    main()
