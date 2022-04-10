

def main():
    """
    This is just a brute force solution.
    """
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums = sorted(nums)

    # First, we need to check if the numbers are even.
    # If they are not even, then it is impossible to construct the matrix.
    if sum(nums) % 2 != 0:
        print("NO")
        return

    # Now we need to check if the numbers are symmetric.
    # If they are not symmetric, then it is impossible to construct the matrix.
    unique_nums = set(nums)
    for num in unique_nums:
        if nums.count(num) % 2 != 0:
            print("NO")
            return

    # Now we need to construct the matrix.
    matrix = [[0 for x in range(n)] for y in range(n)]
    i = 0
    j = 0
    while nums:
        if i == j:
            # We are on the diagonal.
            matrix[i][j] = nums.pop()
            j += 1
            if j >= n:
                i += 1
                j = 0
        else:
            # We are not on the diagonal.
            matrix[i][j] = nums.pop()
            matrix[j][i] = nums.pop()
            j += 1
            if j >= n:
                i += 1
                j = 0
    print("YES")
    for row in matrix:
        print(" ".join([str(x) for x in row]))

if __name__ == '__main__':
    main()