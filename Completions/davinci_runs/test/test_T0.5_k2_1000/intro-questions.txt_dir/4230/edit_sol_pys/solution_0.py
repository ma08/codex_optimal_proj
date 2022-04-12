
n = int(input().split()[0])  # number of houses
x = int(input().split()[0])  # position of the house
p = [int(i) for i in input().split()]  # positions of the houses
p.sort()  # sort the position of the houses

if x <= p[0]:
    print(p[0] - x)
elif x >= p[-1]:
    print(x - p[-1])
else:
    for i in range(1, n):
        if x <= p[i]:
            print(min(x - p[i - 1], p[i] - x))
            break
