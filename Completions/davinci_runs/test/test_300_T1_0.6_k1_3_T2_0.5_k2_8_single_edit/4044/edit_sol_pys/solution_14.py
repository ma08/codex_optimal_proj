
#!/bin/python
#!/usr/bin/env python
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print(arr)
    arr.sort()
    print(arr)
    print(arr[-2])
