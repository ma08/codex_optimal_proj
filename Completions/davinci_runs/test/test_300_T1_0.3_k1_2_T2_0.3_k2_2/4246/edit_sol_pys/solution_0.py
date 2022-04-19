
with open('input.txt', 'r') as f:
    s = f.readline()
    t = f.readline()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)
