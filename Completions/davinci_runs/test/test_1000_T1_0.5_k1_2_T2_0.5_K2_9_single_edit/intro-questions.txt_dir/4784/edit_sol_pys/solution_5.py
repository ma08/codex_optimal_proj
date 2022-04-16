

X = int(input()) # X = 500
N = int(input()) # N = 3

# 300
# 100
# 200

total = X
for i in range(N):
    total -= int(input()) # total = 500 - 300 = 200
                          # total = 200 - 100 = 100
                          # total = 100 - 200 = -100

print(total)
