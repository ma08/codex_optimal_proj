

n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_min_moves(x):
    return sum(x // 2 for x in a)

def is_valid(moves):
    return get_min_moves(moves) <= moves

# Binary search to find the minimum number of moves
low = 0
high = 2 * 10 ** 5
while low < high:
    mid = (low + high) // 2
    if is_valid(mid):
        high = mid
    else:
        low = mid + 1

print(low)