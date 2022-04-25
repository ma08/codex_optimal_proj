A,B,C = map(int, input().split())

count = 0
while B >= A and count < C:
    B -= A
    count += 1
print(count)
