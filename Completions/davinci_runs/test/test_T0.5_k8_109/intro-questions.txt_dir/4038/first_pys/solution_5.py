

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    if n % 2 == 1:
        center = nums[len(nums) // 2]
        nums = nums[:len(nums) // 2] + nums[len(nums) // 2 + 1:]
    else:
        center = None
    if len(nums) % 2 == 1:
        print("NO")
        return
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(len(nums) // 2):
        matrix[i][i] = nums[i]
        matrix[n - i - 1][i] = nums[i]
        matrix[i][n - i - 1] = nums[len(nums) // 2 + i]
        matrix[n - i - 1][n - i - 1] = nums[len(nums) // 2 + i]
    if center is not None:
        matrix[n // 2][n // 2] = center
    print("YES")
    for row in matrix:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()