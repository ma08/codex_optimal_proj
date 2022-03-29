

n = int(input())

hashtags = []

for i in range(n):
    hashtags.append(input())

hashtags.sort()

for i in range(n):
    print(hashtags[i])