"""
    题目：https://www.nowcoder.com/pat/2/problem/253
"""

def swap(p, q):
    return q, p


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    count_p = 0
    count_q = 0
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = swap(P[j], P[i])
                count_p += 1
            if Q[i] > Q[j]:
                Q[i], Q[j] = swap(Q[i], Q[j])
                count += 1
    print(count)


if __name__ == '__main__':
    main()
