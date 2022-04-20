import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


N = int(input())
V = [int(x) for x in input().split()]
V.sort()
while len(V) > 1:
    a = V.pop(0)
    b = V.pop(0)
    V.append((a + b) / 2)
    V.sort()
print(V[0])
