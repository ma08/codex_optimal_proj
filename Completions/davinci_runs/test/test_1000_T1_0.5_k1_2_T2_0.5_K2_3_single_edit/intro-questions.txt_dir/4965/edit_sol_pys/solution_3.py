
n = int(input())
t = list(map(int, input().split()))

# Sort the temperatures
t.sort()

if n == 2:
    print(t[1], t[0])

elif n == 3:
    print(t[2], t[0], t[1])

else:
    if t[-1] - t[0] < t[1] - t[0]:
        print('impossible')

    else:
        print(t[-1], end=' ')
        for i in range(1, n-1):
            print(t[i], end=' ')
        print(t[0])
