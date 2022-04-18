
x = int(input().split()[0]) # The position of the machine
n = int(input().split()[0]) # The number of machines
p = [int(i) for i in input().split()] # The position of the machines
p.sort()

if x <= p[0]:
    print(p[0]-x)
elif x >= p[-1]:
    print(x-p[-1])
else:
    for i in range(1, n):
        if x <= p[i]:
            print(min(x-p[i-1], p[i]-x))
            break
