

def main():
    n, m = map(int, input().split())
    exams = [[] for i in range(m)]
    for i in range(m):
        exams[i] = list(map(int, input().split())) + [i]
    
    for i in range(len(exams)):
        temp = exams[i]
        j = i - 1
        while j >= 0 and exams[j][1] >= temp[1]:
            exams[j+1] = exams[j]
            j -= 1
        exams[j+1] = temp
    
    ans = [0] * n
    for i in range(m):
        for j in range(exams[i][0]-1, exams[i][1]-1):
            if ans[j] == 0:
                ans[j] = exams[i][2] + 1
    
    for i in range(n):
        if ans[i] == 0:
            ans[i] = m + 1
    
    if ans.count(m + 1) > 0:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
