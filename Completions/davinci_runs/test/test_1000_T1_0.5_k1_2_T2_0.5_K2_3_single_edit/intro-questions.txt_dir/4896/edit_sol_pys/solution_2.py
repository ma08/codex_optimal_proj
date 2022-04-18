import sys
n = int(sys.stdin.readline().strip())
bricks = [int(x) for x in sys.stdin.readline().strip().split()]


min_width = bricks[0]
num_towers = 1

for brick in bricks[1:]:
    if brick > min_width:
        num_towers += 1
        min_width = brick

print(num_towers)
