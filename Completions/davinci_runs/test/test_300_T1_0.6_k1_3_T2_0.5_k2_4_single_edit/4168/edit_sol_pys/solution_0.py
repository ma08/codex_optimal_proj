import sys
sys.setrecursionlimit(1000000000)

def main():
    n = int(input())
    ans = []
    if n == 0:
        ans.append("0")

    else:
        def dfs(n):
            if n % 2 == 0:
                ans.append("0")
                n = n // -2
            else:
                ans.append("1")
                n = (n - 1) // -2
            if n != 0:
                dfs(n)
        dfs(n)
        if ans[-1] == '1':
            ans.append("1")
        ans = ans[::-1]

    print(ans)

if __name__ == "__main__":
    main()
