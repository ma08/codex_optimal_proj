
# Code

# Read input as specified in the question.
# Print output as specified in the question.

def min_price(arr):
    # total = sum(arr)
    # max_val = max(arr)
    # if (total - max_val) >= max_val:
    #     return max_val
    # else:
    #     return total//len(arr)
    # return max(sum(arr)//len(arr), max(arr))
    return max(sum(arr)//len(arr), max(arr))


if __name__ == '__main__':
    q = int(input())  # q is the no of queries
    for i in range(q):  # iterate through the queries
        n = int(input())  # n is the no of elements in each query
        arr = list(map(int, input().split()))  # arr is the array of elements
        print(min_price(arr))  # print the result
