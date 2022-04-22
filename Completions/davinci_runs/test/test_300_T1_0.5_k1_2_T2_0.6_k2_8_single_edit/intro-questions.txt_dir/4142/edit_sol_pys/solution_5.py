
import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

s = input()

if (len(s) % 2 == 0) and (s[0] in 'RUD') and (s[-1] in 'RUD') and (all(ch in 'RLUD' for ch in s[1:])):
    print('Yes')
else:
    print('No')
