

#-------------------------------------------------------------------------------
# Name:        Template Matching (Python)
# Purpose:
#
# Author:      chenw_000
#
# Created:     24/02/2013
# Copyright:   (c) chenw_000 2013, 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
import sys

N, M = map(int, raw_input().split())

A = []
for i in range(N):
    A.append(raw_input())

B = []
for i in range(M):
    B.append(raw_input())

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if A[i][j:j+M] == B[0]:
            if A[i:i+M] == B:
                print "Yes"
                sys.exit(0)

print "No"
