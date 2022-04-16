
t = int(input())

for _ in range(t):
    n = int(input())  # number of students
    s = 0
    j = 1
    while s < n:
        s += j
        j *= 2
    print(n//(j//2))
