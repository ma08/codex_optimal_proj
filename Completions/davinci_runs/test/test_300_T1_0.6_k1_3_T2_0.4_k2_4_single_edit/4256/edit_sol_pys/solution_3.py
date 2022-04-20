

# initial input
a, b, c = map(int, input().split())  # a: 初期値, b: 目標値, c: 回数

# count up
count = 0
while count < c and b >= a:
    b -= a
    count += 1

# output
print(count)
