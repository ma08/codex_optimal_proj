import sys

N = int(sys.stdin.readline())

# def solve(N):
#     if N == 0:
#         return 'INSOMNIA'
#     seen = set()
#     for i in range(1, 1000):
#         seen |= set(str(N * i))
#         if len(seen) == 10:
#             return N * i
#     return 'INSOMNIA'

# for i in range(1, N + 1):
#     print('Case #{}: {}'.format(i, solve(int(sys.stdin.readline()))))

s = set()
for i in range(1, 10):
    s.add(i)
print(s)
