#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:45:34 2020

@author: cpprhtn
"""

'''
문제: 
    참가자는 각 팀의 최근 5경기의 승/패 여부를 알고 있다. 
    이 결과를 바탕으로 각 팀의 승률을 계산하고, 
    승률이 높은 팀이 더 많은 승점을 가질 것이라고 예상하는 팀을 출력하는 프로그램을 작성하라.
    
입력: 
    5
    WLLWW
    LWWWW
    WWLWW
    LLLLL
    WLLLL

출력: 
    3 3
'''

n = int(input()) #팀 수

wins = [0] * n
for i in range(n):
    matches = input()
    for match in matches:
        if match == 'W':
            wins[i] += 1

print(wins.count(max(wins)), wins.count(min(wins)))
