import sys

s = sys.stdin.readline()

s = s.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')

print(s.split())
