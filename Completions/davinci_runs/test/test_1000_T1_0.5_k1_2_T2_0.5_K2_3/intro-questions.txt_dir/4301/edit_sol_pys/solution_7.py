

n = int(input())
array = [int(input()) for _ in range(n)]
max_array = max(array)
print(*[max_array if x == max_array else max_array - 1 for x in array])
