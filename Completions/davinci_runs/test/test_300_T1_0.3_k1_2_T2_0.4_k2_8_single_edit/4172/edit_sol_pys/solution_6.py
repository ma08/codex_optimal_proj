

def min_moves(arr):
    min_val = min(arr)
    max_val = max(arr)
    return max_val - min_val

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_moves(arr))
