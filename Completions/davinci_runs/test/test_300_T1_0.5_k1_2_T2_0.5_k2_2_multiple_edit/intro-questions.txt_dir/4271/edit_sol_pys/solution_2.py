n = int(input())
dishes = list(map(int, input().split()))

ans = ''
for i in range(n):
    if dishes[i] == 1:
        ans += 'A'
    elif dishes[i] == 2:
        ans += 'B'
    elif dishes[i] == 3:
        ans += 'C'
    elif dishes[i] == 4:
        ans += 'D'
    elif dishes[i] == 5:
        ans += 'E'

print(ans, end='')
