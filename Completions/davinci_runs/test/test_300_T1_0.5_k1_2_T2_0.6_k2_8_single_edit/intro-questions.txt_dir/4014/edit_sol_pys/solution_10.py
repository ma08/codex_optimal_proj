

def main():
    n, m = map(int, input().split())
    exams = [list(map(int, input().split())) for _ in range(m)]
    
    exams.sort(key=lambda x: x[1])
    
    ans = [0] * n
    for i in range(m):
        for j in range(exams[i][0], exams[i][1]):
            if ans[j] == 0:
                ans[j] = i + 1
    
    for i in range(n):
        if ans[i] == 0:
            ans[i] = m + 1
    
    if ans.count(m + 1) < m:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
