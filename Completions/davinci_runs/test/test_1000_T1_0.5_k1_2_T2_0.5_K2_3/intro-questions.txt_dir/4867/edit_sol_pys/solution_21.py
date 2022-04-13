
import sys
import math

# Grab the pellets as fast as you can

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]

# Print an error message, because the maze is too small
if width < 10 or height < 10:
    print("The maze is too small!")
    sys.exit(0)

# game loop
while True:
    # x: Pac-Man's x position
    # y: Pac-Man's y position
    # pac_id: Pac-Man's unique id
    # mine: true if this pac is yours
    x, y, pac_id, mine = [int(j) for j in input().split()]

    # visible_pac_count: all your pacs and enemy pacs in sight
    # mine_count: number of visible pellets in sight
    visible_pac_count, mine_count = [int(i) for i in input().split()]
    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this Pac-Man is powered up, false otherwise
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        mine = mine != "0"
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)

    # visible_pellet_count: all pellets in sight
    visible_pellet_count = int(input())
    pellets = []
    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, value = [int(j) for j in input().split()]
        pellets.append((x, y, value))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # MOVE <pacId> <x> <y>
    print("MOVE %d %d %d" % (pac_id, x+1, y))
