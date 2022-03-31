
def main():
    n = int(input())
    s = [int(x) for x in input().split()]  # list comprehension
    prefix = [0]
    for i in range(n):  # O(n)
        prefix.append(prefix[-1] + s[i])

    prefix.sort()
    count = 0
    for i in range(1, n + 1):  # O(n)
        if prefix[i] == prefix[i - 1]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
