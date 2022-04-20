

input()
print(len(set(map(sum, [list(map(int, input().split()[i:j])) for i in range(7) for j in range(i+1, 8)]))))