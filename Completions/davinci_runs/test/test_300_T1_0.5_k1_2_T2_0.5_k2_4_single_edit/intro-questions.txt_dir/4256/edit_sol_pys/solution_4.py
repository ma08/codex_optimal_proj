
A,B,C = map(int, input().split())

if B < A:
    print(0)
else:
    count = 0
    while B >= A and count < C:
        B -= A
        count += 1
    print(count)
