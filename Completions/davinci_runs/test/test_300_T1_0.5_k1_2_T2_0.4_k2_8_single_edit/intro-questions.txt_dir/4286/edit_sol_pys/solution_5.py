
import sys
sys.setrecursionlimit(10**6)
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]

    a.sort()
    b.sort()

    if a[0] < b[-1]:
        print(-1)
        return

    a_idx = 0
    b_idx = 0
    while a_idx < n:
        while a[a_idx] < b[b_idx]:
            a_idx += 1
            if a_idx >= n:
                break

        if a_idx >= n:
            break

        a[a_idx] = b[b_idx]
        a_idx += 1
        b_idx += 1

    print(sum(a))


if __name__ == "__main__":
    main()
