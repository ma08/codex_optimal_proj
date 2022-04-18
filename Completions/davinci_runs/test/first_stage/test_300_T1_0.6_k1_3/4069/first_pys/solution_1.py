
def takahashi_traveling(x, k, d):
    if k <= (x // d):
        return x - k * d
    else:
        return abs(x - d * ((x // d) + 1))

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))


"""
Takahashi is now at coordinate 6. It is optimal to make the following moves:
 - Move from coordinate 6 to (6 - 4 =) 2.
 - Move from coordinate 2 to (2 - 4 =) -2.
Here, the absolute value of the coordinate of the destination is 2, and we cannot make it smaller.
"""
def takahashi_traveling(x, k, d):
    if k <= (x // d):
        return x - k * d
    else:
        return abs(x - d * ((x // d) + 1))

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))