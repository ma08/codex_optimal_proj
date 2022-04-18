

n, k = map(int, input().split())
throws = input().split()

position = 0

for i in range(k):
    if throws[i] == 'undo':
        position += int(throws[i+1])
    else:
        position += int(throws[i])
        if position > n-1:
            position -= n
        elif position < 0:
            position += n

print(position)