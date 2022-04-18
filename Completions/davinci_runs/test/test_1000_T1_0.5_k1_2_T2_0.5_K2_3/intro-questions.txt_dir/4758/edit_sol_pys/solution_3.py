with open("input.txt", "r") as f:
    N, T, M = map(int, f.readline().split())

with open("output.txt", "w") as f:
    f.write(str(N * T * M))
