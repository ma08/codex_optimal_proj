

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    matrix = [[0 for i in range(n)] for j in range(n)]
    if n % 2 == 1:
        matrix[n // 2][n // 2] = nums.pop()
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j] = nums.pop()
            matrix[i][n - j - 1] = matrix[i][j]
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j] = nums.pop()
            matrix[n - i - 1][j] = matrix[i][j]
    if len(nums) == 0:
        print("YES")
        for i in range(n):
            print(' '.join(map(str, matrix[i])))
    else:
        print("NO")

if __name__ == "__main__":
    main()