import queue

def main():
    q = queue.Queue()
    q.put(0)
    q.put(1)
    q.put(2)

    for i in range(1, n+1):
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:
        for j in range(c, m):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
