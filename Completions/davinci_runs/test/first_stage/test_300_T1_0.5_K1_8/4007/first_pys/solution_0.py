

n = int(input())
f = list(map(int, input().split()))

# First, fill in the gift-giving for people who don't know where to give their gift to
for i in range(len(f)):
    if f[i] == 0:
        for j in range(len(f)):
            if f[j] == 0:
                f[i] = j + 1
                break
        break

# Now, fill in the gift-giving for people who don't know where to receive their gift from
for i in range(len(f)):
    if f[i] == 0:
        for j in range(len(f)):
            if f[j] == 0:
                f[i] = j + 1
                break
        break

# Now, fill in the gift-giving for people who don't know where to give their gift to
for i in range(len(f)):
    if f[i] == 0:
        for j in range(len(f)):
            if f[j] == 0:
                f[i] = j + 1
                break
        break

print(*f)