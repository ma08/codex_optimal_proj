
from collections import Counter

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    # print(N,A)

    c = Counter(A)
    # print(c)

    A_u = list(set(A))
    A_u.sort()
    # print(A_u)

    s = 0
    for i in A_u:
        s += c[i]*(N-c[i])
    # print(s)

    print(s//2)

if __name__ == '__main__':
    main()
