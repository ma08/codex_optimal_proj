
#-------------------------------------------------------------------------------
# Name:        Template Matching2
# Purpose:
#
# Author:      chenw_000
#
# Created:     24/02/2013
# Copyright:   (c) chenw_000 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def main():
    pass

if __name__ == '__main__':
    main()

N, M = map(int, raw_input().split())

A = []
for i in range(N):
    A.append(raw_input())

B = []
for i in range(M):
    B.append(raw_input())

def find_sub_matrix(A, B, N, M):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if A[i][j:j+M] == B[0]:
                if A[i:i+M] == B:
                    return True
    return False

if find_sub_matrix(A, B, N, M):
    print "Yes"
else:
    print "No"
