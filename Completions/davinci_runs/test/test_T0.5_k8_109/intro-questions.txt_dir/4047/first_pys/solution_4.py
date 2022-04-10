

#-----Solution-----

n = int(input())
x = [int(i) for i in input().split()]

min_x = min(x)
max_x = max(x)

print(min(max_x - min_x, (max_x - min_x) // 2 + (max_x - min_x) % 2))