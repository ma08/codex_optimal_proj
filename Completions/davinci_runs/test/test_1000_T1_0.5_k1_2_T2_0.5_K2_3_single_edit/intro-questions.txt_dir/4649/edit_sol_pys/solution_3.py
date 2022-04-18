

def rgb_substring(s, k):
    if k > len(s):
        return -1
    if k == len(s):
        return 0
    return -1


def main():
    q = int(input())
    for _ in range(q):
        n, k = [int(x) for x in input().split()]
        s = input()
        print(rgb_substring(s, k))


if __name__ == "__main__":
    main()
