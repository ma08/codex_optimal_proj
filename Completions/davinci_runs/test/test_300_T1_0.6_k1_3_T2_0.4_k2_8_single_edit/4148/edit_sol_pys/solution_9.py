import sys
input = sys.stdin.readline


n = int(input())
s = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for si in s:
    print(alphabet[(alphabet.index(si) + n) % 26], end="")
