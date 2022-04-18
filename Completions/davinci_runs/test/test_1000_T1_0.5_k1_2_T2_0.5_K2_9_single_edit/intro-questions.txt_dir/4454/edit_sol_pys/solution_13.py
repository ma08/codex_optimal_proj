

# Code

## Read input as specified in the question.
## Print output as specified in the question.

def min_price(arr):
    # total = sum(arr)
    # max_val = max(arr)
    # if (total - max_val) >= max_val:
    #     return max_val
    # else:
    #     return total//len(arr)
    return sum(arr)//len(arr)

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_price(arr))
