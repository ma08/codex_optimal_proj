import sys


N = int(sys.stdin.readline())
costumes = set(sys.stdin.readline().strip() for _ in range(N))

costumes = list(costumes)
costumes.sort()
for costume in costumes:
    print(costume)
