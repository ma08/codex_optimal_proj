

#==================================================================
#=============================CODE=================================
#==================================================================
from collections import deque

import sys

def main():
    input = sys.stdin.readline()
    n = int(input)
    input = sys.stdin.readline().split().reverse()
    queue = deque()
    for i in input:
        queue.append(int(i))
    print(queue)

main()
