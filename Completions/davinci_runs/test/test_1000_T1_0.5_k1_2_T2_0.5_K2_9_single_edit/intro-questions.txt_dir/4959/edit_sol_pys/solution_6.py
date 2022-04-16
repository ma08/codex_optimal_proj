#!/usr/bin/env python3

def soda(e,f,c):
    bottles = e + f
    drinks = 0
    while bottles >= c:
        drinks += 1
        bottles -= c
        bottles += 1
    return drinks

if __name__ == "__main__":
    e,f,c = map(int,input().split())
    print(soda(e,f,c))
