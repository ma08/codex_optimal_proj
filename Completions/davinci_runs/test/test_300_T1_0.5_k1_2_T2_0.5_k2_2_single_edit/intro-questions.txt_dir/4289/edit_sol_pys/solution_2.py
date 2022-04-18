
import sys

input = sys.stdin.readline

n = int(input())  # number of people
t, a = map(int, input().split())  # target temperature and temperature of the place
h = [int(input()) for i in range(n)]  # heights of the people

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
