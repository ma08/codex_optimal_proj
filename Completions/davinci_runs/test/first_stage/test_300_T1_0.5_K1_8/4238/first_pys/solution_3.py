

N = int(input())

print(['No', 'Yes'][sum(map(int, list(str(N)))) % 9 == 0])