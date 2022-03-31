

def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + s[i])

    prefix.sort()
    count = 0
    for i in range(1, n + 1):
        if prefix[i] == prefix[i - 1]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()