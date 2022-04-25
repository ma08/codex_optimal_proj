
import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
