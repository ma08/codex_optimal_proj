

def main():
    n, m = map(int, input().split())
    exams = [[0,0,0]] * (m + 1)
    for i in range(m):
        exams[i] = list(map(int, input().split()))
    
    for i in range(1, len(exams)):
        temp = exams[i]
        j = i
        while j > 0 and exams[j-1][1] > temp[1]:
            exams[j+1] = exams[j]
            j -= 1
        exams[j+1] = temp
    
    ans = [0] * n
    for i in range(1, m + 1):
        for j in range(exams[i][0] - 1, exams[i][1]):
            if ans[j] == 0:
                ans[j] = i
    
    for i in range(n):
        if ans[i] == 0:
            ans[i] = m
    
    if ans.count(m) < m:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
