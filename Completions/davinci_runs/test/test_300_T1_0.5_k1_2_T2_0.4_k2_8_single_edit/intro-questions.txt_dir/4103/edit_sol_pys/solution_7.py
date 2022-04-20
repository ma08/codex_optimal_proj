

n, k = map(int, input().split())
s = list(map(int, input().split())) + [0]

segments = 0
current_segment = 0
for i in range(n + 1):
    if s[i] == 1:
        current_segment += 1
    else:
        if current_segment > 0:
            segments += current_segment // k
            current_segment = current_segment % k
        segments += 1
        current_segment = 0

print(segments)
