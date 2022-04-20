#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:06:17 2020
@author: ritambasu
"""

n, x = map(int, input().split())
cities = list(map(int, input().split()))

# Find the minimum distance between the starting point and the cities
min_dist = min([abs(x - city) for city in cities])

# Find the maximum distance between the cities
max_dist = max([abs(city1 - city2) for city1 in cities for city2 in cities])

# Find the maximum distance that can be traveled
print(max(min_dist, max_dist // 2))
