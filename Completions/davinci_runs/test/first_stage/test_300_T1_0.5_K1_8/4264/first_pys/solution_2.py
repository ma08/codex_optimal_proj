

n = input()

print(len(list(filter(lambda x: len(x) % 2 == 1, [str(i) for i in range(1, int(n) + 1)]))))