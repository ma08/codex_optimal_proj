#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:02:38 2020

@author: tomasferrer
"""

def next_player(pl):
    if pl == 0:
        return 7
    else:
        return pl-1
    

k, n = map(int, input().split())
players = [False for i in range(8)]
players[k-1] = True
for i in range(n):
    time, ans = map(str, input().split())
    time = int(time)
    if ans == 'T':
        pass
    elif ans == 'N':
        players = [False for i in range(8)]
    elif ans == 'P':
        players = [False for i in range(8)]
        players[next_player(k-1)] = True
    if time >= 210:
        print(players.index(True)+1)
        break
    else:
        players = [False for i in range(8)]
        players[next_player(players.index(True))] = True
