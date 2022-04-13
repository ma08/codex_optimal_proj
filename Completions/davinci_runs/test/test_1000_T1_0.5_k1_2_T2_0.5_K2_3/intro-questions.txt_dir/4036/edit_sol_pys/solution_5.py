import sys

def main():
    sys.setrecursionlimit(1000000000)
    n, k = map(int, input().split())
    if(n == 1 and k == 1):
        print("yes")
        print("1")
    elif(n < k):
        print("no")
    elif(n > k):
        a = [0] * k
        a[k-1] = n
        dfs(0, a, k, n)
    else:
        print("no")

def dfs(i, a, k, n):
    if(i == k):
        if(sum(a) == n):
            print("yes")
            print(" ".join(map(str, a)))
            exit()
    else:
        for j in range(1, n + 1):
            a[i] = j
            dfs(i + 1, a, k, n)

if __name__ == "__main__":
    main()
