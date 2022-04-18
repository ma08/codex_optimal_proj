

from collections import Counter

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    cnt = Counter(A)
    #print(cnt)
    if cnt[0] > 0:
        print(0)
        return

    ans = 1
    for k, v in cnt.items():
        if k > 0:
            ans *= (v + 1)

    print(ans % (10**9 + 7))

if __name__ == "__main__":
    main()
