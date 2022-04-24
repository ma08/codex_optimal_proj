

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segments = 1
cur_a = a
cur_b = b
for i in range(n):
    if s[i] == 1:
        if cur_b > 0:
            cur_b -= 1
        else:
            if cur_a == 0:
                break
            cur_a -= 1
    else:
        if cur_a > 0:
            cur_a -= 1
            if cur_a == 0:
                break
        else:
            cur_b -= 1
            if cur_b == 0:
                break
    if cur_a == 0 or cur_b == 0:
        break
    max_segments += 1
print(max_segments)
