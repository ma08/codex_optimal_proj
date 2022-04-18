import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout


N = int(input())
bricks = list(map(int, f.readline().split()))

towers = 1

for i in range(1, N):
    if bricks[i] > bricks[i-1]:
        towers += 1

print(towers)
