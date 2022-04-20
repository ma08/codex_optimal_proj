

from sys import stdin

a,b,c = [int(x) for x in stdin.readline().split()]

print(min(a,b,c)*7)