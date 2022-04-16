


n = int(input())

languages = list(map(int, input().split()))

last_position = {}

min_distance = n

for i in range(n):
    if languages[i] in last_position:
        min_distance = min(min_distance, i - last_position[languages[i]])
    last_position[languages[i]] = i

print(min_distance)
