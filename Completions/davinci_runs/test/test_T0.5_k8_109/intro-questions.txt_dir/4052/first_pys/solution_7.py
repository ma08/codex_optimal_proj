


def get_swaps(s, t):
    if s == t:
        return 0, []
    swaps = []
    for i in range(len(s) - 1):
        if s[i:i+2] == t[i:i+2]:
            continue
        if s[i:i+2] == t[i+1:i+3]:
            swaps.append(i)
            s = s[:i] + t[i:i+2] + s[i+2:]
        elif s[i:i+2] == t[i-1:i+1]:
            swaps.append(i-1)
            s = s[:i-1] + t[i-1:i+1] + s[i+1:]
    return len(swaps), swaps


def main():
    n = int(input())
    s = input()
    t = input()
    k, swaps = get_swaps(s, t)
    if k > 10000:
        print(-1)
    else:
        print(k)
        print(*swaps)


if __name__ == "__main__":
    main()