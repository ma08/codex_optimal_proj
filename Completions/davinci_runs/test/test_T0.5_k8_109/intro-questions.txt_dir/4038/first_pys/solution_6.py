

import math

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    if len(numbers) != n**2:
        print("NO")
        return
    numbers.sort()
    if numbers[0] != numbers[-1]:
        print("NO")
        return
    if n%2 == 0:
        if numbers[0] != numbers[n**2//2]:
            print("NO")
            return
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(-1)
    if n%2 == 1:
        matrix[n//2][n//2] = numbers[0]
        numbers.pop(0)
    for i in range(n//2):
        for j in range(n//2):
            matrix[i][j] = numbers[0]
            matrix[i][n-j-1] = numbers[0]
            matrix[n-i-1][j] = numbers[0]
            matrix[n-i-1][n-j-1] = numbers[0]
            numbers.pop(0)
    if len(numbers) != 0:
        print("NO")
        return
    print("YES")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

if __name__ == '__main__':
    main()