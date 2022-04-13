
from sys import stdin, stdout

s = stdin.readline().strip()

# Check if there are an odd number of both black and white stones
if s.count('B') % 2 == 1 and s.count('W') % 2 == 1:
    stdout.write('0')
# Check if there are an even number of both black and white stones
elif s.count('B') % 2 == 0 and s.count('W') % 2 == 0:
    stdout.write('1')
# Check if there are an even number of black stones and an odd number of white stones
elif s.count('B') % 2 == 0:
    if 'WWBWWB' in s or 'BWWBWW' in s:
        stdout.write('1')
    else:
        stdout.write('0')
# Check if there are an odd number of black stones and an even number of white stones
else:
    if 'WWBWWB' in s or 'BWWBWW' in s:
        stdout.write('1')
    else:
        stdout.write('0')
