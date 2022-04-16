

n = int(input())
t = list(map(int, input().split()))

# Sort the temperatures in descending order
t.sort(reverse=True)

# If the input is impossible
if t[-1] - t[0] < t[1] - t[0]:
    print('impossible')
# If the input is possible
else:
    print(t[-1], end=' ')
    for i in range(1, n-1):
        print(t[i], end=' ')
    print(t[0])
