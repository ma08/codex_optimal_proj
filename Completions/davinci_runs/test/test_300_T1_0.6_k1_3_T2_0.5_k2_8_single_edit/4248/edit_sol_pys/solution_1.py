#! /usr/bin/env python3

import sys
import math

def read_data(file_name):
	S = []
	with open(file_name, 'r') as file:
		n = int(file.readline().strip())
		for i in range(n):
			x, y = [float(x) for x in file.readline().strip().split()]
			S.append((x,y))
	return S

def is_left(a,b,c):
	return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])

def area(a,b,c):
	return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])

def convex_hull(S):
	n = len(S)
	S.sort()
	P = [S[0],S[1]]
	for i in range(2,n):
		while len(P)>1 and is_left(P[-2],P[-1],S[i])<=0:
			P.pop()
		P.append(S[i])
	U = [P[-1],P[0]]
	for i in range(n-2,-1,-1):
		while len(U)>1 and is_left(U[-2],U[-1],S[i])<=0:
			U.pop()
		U.append(S[i])
	return P,U

def find_angle(S):
	n = len(S)
	if n<=2:
		return 0
	P,U = convex_hull(S)
	A = 0
	for i in range(len(P)-1):
		A += area(P[i],P[i+1],U[i])
	A += area(P[-1],P[0],U[-1])
	A = abs(A)/2
	area_sum = 0
	for i in range(len(P)-1):
		area_sum += area(P[i],P[i+1],(0,0))
	area_sum += area(P[-1],P[0],(0,0))
	area_sum = abs(area_sum)/2
	return A/area_sum

S = read_data(sys.argv[1])
print(find_angle(S))
