

import heapq
import math

def main():
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))#coding:utf-8
    # heapq.heappush(h, (a, i))

if __name__ == '__main__':
    main()
