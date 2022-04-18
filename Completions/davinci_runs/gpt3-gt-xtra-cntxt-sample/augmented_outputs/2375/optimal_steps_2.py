def three_block_palindrome(n, a, t):
    a.sort()
    answer = 0
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and a[i] == a[i + 1]:
            i += 1
            count += 1
        if count > 2:
            answer += count
        elif count == 2:
            answer += count - 1
        i += 1
    print("Case #{}: {}".format(t, answer))

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        three_block_palindrome(n, a, i + 1)