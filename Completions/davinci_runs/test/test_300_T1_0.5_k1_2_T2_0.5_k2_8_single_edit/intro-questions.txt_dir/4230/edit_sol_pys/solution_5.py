

x = int(input()) # number of pages
n = int(input()) # number of chapters
p = list(map(int, input().split())) # array of pages of each chapter

p.sort()

if x < p[0]:
    print(p[0] - x)
elif x > p[n-1]:
    print(x - p[n-1])
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                print(p[i-1] - x)
            else:
                print(p[i] - x)
            break
