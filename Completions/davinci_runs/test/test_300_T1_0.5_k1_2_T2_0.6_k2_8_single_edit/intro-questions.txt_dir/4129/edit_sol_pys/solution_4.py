#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file.py
#  
#  Copyright 2014 Ajay Bhatia <ajay@dumb-box>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
from collections import defaultdict

def dfs(v, visited):
	visited[v] = True
	for u in rev_adj_list[v]:
		if not visited[u]:
			dfs(u, visited)

def main():
	global rev_adj_list
	n, m, s = map(int, sys.stdin.readline().split())
	adj_list = defaultdict(list)
	rev_adj_list = defaultdict(list)
	for _ in range(m):
		u, v = map(int, sys.stdin.readline().split())
		adj_list[u].append(v)
		rev_adj_list[v].append(u)
	visited = [False] * (n + 1)
	dfs(s, visited)
	count = 0
	for v in range(1, n + 1):
		if not visited[v]:
			for u in adj_list[v]:
				if visited[u]:
					count += 1
					break
	print count

if __name__ == '__main__':
	main()
