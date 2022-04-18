#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def main():
    n, h, l = map(int, input().split())
    horror = set(map(int, input().split()))
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a-1].append(b-1)
        similar[b-1].append(a-1)
    horror_index = [0] * n
    for i in range(n):
        if i+1 not in horror:
            horror_index[i] = max(horror_index[j] for j in similar[i]) + 1
    print(horror_index.index(max(horror_index))+1)

main()
