

n, c = map(int, input().split()) # n is the number of elements in the array, c is the range of numbers in the array
arr = list(map(int, input().split())) # input array

freq = [0] * (c + 1)
for i in range(n):
    freq[arr[i]] += 1

for i in range(c + 1):
    if freq[i] > 0:
        print((str(i) + ' ') * freq[i], end='')
