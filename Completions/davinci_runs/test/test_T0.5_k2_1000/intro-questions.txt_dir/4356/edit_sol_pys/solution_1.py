
#-------------------------------------------------------------------------------
# Name:        Template Matching
# Purpose:
#
# Author:      chenw_000
#
# Created:     24/02/2013
# Copyright:   (c) chenw_000 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, copy

N, M = map(int, raw_input().split())

A = [raw_input() for i in range(N)]
B = [raw_input() for i in range(M)]

def check(i, j):
    for k in range(M):
        if A[i+k][j:j+M] != B[k]:
            return False
    return True

def rotate(B):
    B = copy.deepcopy(B)
    for i in range(M):
        for j in range(M):
            B[i][j] = B[M-j-1][i]
    return B

print "No"
