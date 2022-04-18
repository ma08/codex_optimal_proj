

def main():
    n, m = map(int, input().split())
    exams = [[0,0,0]] * m
    for i in range(m):
        exams[i] = list(map(int, input().split()))
    
    for i in range(len(exams)):
        temp = exams[i]
        j = i - 1
        while j >= 0 and exams[j][1] > temp[1]:
            exams[j+1] = exams[j]
            j -= 1
        exams[j+1] = temp
    
    ans = [m + 1] * n
    for i in range(m):
        for j in range(exams[i][0], exams[i][1]):
            if ans[j] == m + 1:
                ans[j] = i + 1
    
    if ans.count(m + 1) > m:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
