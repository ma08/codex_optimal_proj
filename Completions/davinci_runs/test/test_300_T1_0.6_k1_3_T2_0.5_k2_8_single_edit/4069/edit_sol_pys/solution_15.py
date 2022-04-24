

"""
Takahashi is now at coordinate 6. It is optimal to make the following moves:
 - Move from coordinate 6 to (6 - 4 =) 2.
 - Move from coordinate 2 to (2 - 4 =) -2.
Here, the absolute value of the coordinate of the destination is 2, and we cannot make it smaller.
"""

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))
