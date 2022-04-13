'''

h, n, m = map(int, input().split()) #height, number of logs, number of pieces of wood

a = 0
b = 0

for i in range(1, h+1):
    a += (2*i - 1) #number of logs
    b += (2*i) #number of pieces of wood

if a <= n:
    print(0, m)
else:
    a -= n
    if a <= m*2: # if we can make the difference between the logs and the pieces of wood
        print(a//2, m - (a//2)) # print the number of logs we can make and the number of pieces of wood left
    else:
'''

h, n, m = map(int, input().split())

a = 0
b = 0

for i in range(1, h+1):
    a += (2*i - 1)
    b += (2*i)

if a <= n:
    print(0, m)
else:
    a -= n
    if a <= m*2:
        print(a//2, m - (a//2))
    else:
        print(m, 0)
        print(m, 0)
