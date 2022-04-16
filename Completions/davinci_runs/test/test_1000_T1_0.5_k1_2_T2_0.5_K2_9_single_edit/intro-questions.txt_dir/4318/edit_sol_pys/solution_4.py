
import sys, collections
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    k = list(map(int, input().split()))
    d = collections.defaultdict(list)
    for i, val in enumerate(arr):
        d[val].append(i)
    for val in k:
        if val not in d:
            print(-1)
        else:
            print(d[val][0] + 1)
            d[val] = d[val][1:]

if __name__ == "__main__":
    main()
