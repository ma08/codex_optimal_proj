import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    arr = []
    for i in range(n):
        arr.append(sys.stdin.readline().strip())
    count = 0
    for j in range(m):
        if arr[0][j] == '_':
            count += 1
            while j < m and arr[0][j] == '_':
                j += 1
    print(count)

if __name__ == "__main__":
    main()
