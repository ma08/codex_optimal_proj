
N = int(input())
S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for s in S:
    print(alphabet[(alphabet.index(s) + N) % 26], end='')
