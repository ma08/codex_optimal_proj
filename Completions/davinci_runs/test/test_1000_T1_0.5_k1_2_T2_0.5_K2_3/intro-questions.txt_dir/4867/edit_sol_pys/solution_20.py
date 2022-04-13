#!/usr/bin/env python3
import sys

# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]

# Print an error message, because the maze is too small.
if width < 10 or height < 10:
    print("The maze is too small!")
    sys.exit(0)

# game loop
while True:
    # x: your pacman's x position
    # y: your pacman's y position
    # pac_id: your pacman's unique id
    # mine: true if this pacman is yours, false otherwise
    x, y, pac_id, mine = [int(j) for j in input().split()]

    # visible_pac_count: all your pacmans and enemy pacmans in sight
    # mine_count: number of visible pellets
    visible_pac_count, mine_count = [int(i) for i in input().split()]
    for i in range(visible_pac_count):
        # pac_id: unique id of this pacman
        # mine: true if this pacman is yours
        # x: position in the grid of this pacman
        # y: position in the grid of this pacman
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = [int(j) for j in input().split()]
        pac_id = int(pac_id)
        mine = mine != "0"
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)


    # visible_pellet_count: all pellets in sight
    visible_pellet_count = int(input())
    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        value = int(input())

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # MOVE <pacId> <x> <y>
    print("MOVE %d %d %d" % (pac_id, x+1, y))
