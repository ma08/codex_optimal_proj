
N = input()

print(["No", "Yes"][sum(map(int, N)) % 9 == 0])
