

N = int(input())
S = input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for s in S:
    print(alphabet[(alphabet.index(s) + N) % 26], end="")