

def main():
    n, m = map(int, input().split())
    exams = [[0,0,0]] * (m+1)
    for i in range(m):
        exams[i] = list(map(int, input().split()))+[i+1]
    
    for i in range(len(exams)):
        temp = exams[i]
        j = i - 1
        while j >= 0 and exams[j][1] < temp[1]:
            exams[j+1] = exams[j]
            j -= 1
        exams[j+1] = temp
    
    ans = [m+1] * n
    for i in range(m):
        for j in range(exams[i][0], exams[i][1]):
            ans[j] = exams[i][2]
    print(*ans)

if __name__ == "__main__":
    main()
