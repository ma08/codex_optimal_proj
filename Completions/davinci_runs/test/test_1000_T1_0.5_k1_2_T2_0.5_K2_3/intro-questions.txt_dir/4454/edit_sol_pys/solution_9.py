

# Code

## Read input as specified in the question
## Print output as specified in the question

def find_max_len(n, arr):
    i = 0
    j = n-1
    count = 0
    while i < j:
        if arr[i] == 0:
            count += 1
            i += 1
        elif arr[j] == 1:
            j -= 1
            count += 1
        else:
            i += 1
            j -= 1
    return count


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_max_len(n, arr))
