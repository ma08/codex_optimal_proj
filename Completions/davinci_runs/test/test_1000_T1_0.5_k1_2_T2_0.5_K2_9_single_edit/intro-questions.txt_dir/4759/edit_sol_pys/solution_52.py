
import sys

n = int(sys.stdin.readline())
bases = list(map(int, sys.stdin.readline().split()))

print(sum(bases) / len([base for base in bases if base != -1]))
