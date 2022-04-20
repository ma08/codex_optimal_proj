
n = int(input())
a = list(map(int, input().split()))

oddSum = [0]
evenSum = [0]

for i in range(1, n+1):
    if i % 2 == 0:
        evenSum.append(evenSum[-1]+a[i-1])
        oddSum.append(oddSum[-1])
    else:
        oddSum.append(oddSum[-1]+a[i-1])
        evenSum.append(evenSum[-1])

count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        if evenSum[i-1] == oddSum[-1]-oddSum[i]:
            count += 1
    else:
        if oddSum[i-1] == evenSum[-1]-evenSum[i]:
            count += 1

print(count)