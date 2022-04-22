import sys

N, M = map(int, sys.stdin.readline().rstrip().split())


list_numbers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


list_numbers.sort(key=lambda x: x[0])
list_numbers.sort(key=lambda x: x[1])

for i in range(N):
    print(list_numbers[i][0], list_numbers[i][1])
