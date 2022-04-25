N = int(input())#input the number of the number
h = list(map(int,input().split()))#input the number

count = 0
for i in range(N):
    if h[i] > count:
        count = h[i]
print(count)
