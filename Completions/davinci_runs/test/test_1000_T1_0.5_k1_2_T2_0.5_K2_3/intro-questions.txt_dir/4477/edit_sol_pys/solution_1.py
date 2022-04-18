'''
Problem statement: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/the-rise-of-the-weird-things-1/
'''


def solve(n, k, x, a):
    a.sort()
    num_weird = 0
    for i in range(n-1):
        if a[i+1] - a[i] == x:
            num_weird += 1
            if num_weird == k:
                return a[i+1]
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, x = list(map(int, input().split()))
        a = list(map(int, input().split()))
        print(solve(n, k, x, a))
