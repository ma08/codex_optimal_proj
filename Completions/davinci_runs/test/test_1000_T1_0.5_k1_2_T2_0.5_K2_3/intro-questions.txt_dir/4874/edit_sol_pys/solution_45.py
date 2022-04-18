
import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    arr = []
    for i in range(n):
        arr.append(sys.stdin.readline().strip())
    count = 0
    j = 0
    while j < m:
        if arr[0][j] != '_':
            j += 1
            continue
        count += 1
        while j < m and arr[0][j] == '_':
            j += 1
    print(count)

main()
