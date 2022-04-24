
import sys
def get_min_operations(n, x, y, num):
    if x < y:
        num = num[:x]
    else:
        num = num[:x] + "0"*(x-y)
    return num.count('0')
if __name__ == "__main__":
    n, x, y = map(int, sys.stdin.readline().strip().split())
    num = sys.stdin.readline().strip()
    print(get_min_operations(n, x, y, num))
