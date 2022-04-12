import sys

N = int(sys.stdin.readline())
costumes = set()  # use set to remove duplicates
for _ in range(N):
    costumes.add(sys.stdin.readline().strip())

costumes = list(costumes)  # convert set to list
costumes.sort()
for costume in costumes:
    print(costume)
