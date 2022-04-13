
import sys
import math


width, height = [int(i) for i in input().split()]

if width < 10 or height < 10:
    print("The maze is too small!")
    sys.exit(0)

# game loop
while True:
    x, y, pac_id, mine = [int(j) for j in input().split()]

    visible_pac_count, mine_count = [int(i) for i in input().split()]
    for i in range(visible_pac_count):
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        mine = mine is not "0"
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)

    visible_pellet_count = int(input())
    pellets = []
    for i in range(visible_pellet_count):
        x, y, value = [int(j) for j in input().split()]
        pellets.append((x, y, value))

    print("MOVE %d %d %d" % (pac_id, x+1, y))
