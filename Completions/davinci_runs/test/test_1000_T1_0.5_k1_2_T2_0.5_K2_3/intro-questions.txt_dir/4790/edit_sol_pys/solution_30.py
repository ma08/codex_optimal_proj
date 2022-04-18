


"""
We will use the following observations to solve this problem:
1) If there are an odd number of black stones and an odd number of white stones, then it is impossible to balance the stone
2) If there are an even number of both black and white stones, then it is always possible to balance the stone
3) If there are an even number of black stones and an odd number of white stones (or vice versa), then it is possible to balance the stone if and only if there is a substring of the form wwbwwbwwbwwb...wbwwbwwbwwb
"""

from sys import stdin, stdout

s = stdin.readline().strip()

# Check if there are an odd number of both black and white stone
if s.count('B') % 2 == 1 and s.count('W') % 2 == 1:
    stdout.write('0')
# Check if there are an even number of both black and white stone
elif s.count('B') % 2 == 0 and s.count('W') % 2 == 0:
    stdout.write('1')
# Check if there are an even number of black stone and an odd number of white stone
elif s.count('B') % 2 == 0:
    if 'WWBWWB' in s or 'BWWBWW' in s:
        stdout.write('1')
    else:
        stdout.write('0')
# Check if there are an odd number of black stone and an even number of white stone
else:
    if 'WWBWWB' in s or 'BWWBWW' in s:
        stdout.write('1')
    else:
        stdout.write('0')
