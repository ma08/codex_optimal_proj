


def main():
    n = int(input())
    s = input()

    # We'll keep track of the number of consecutive letters.
    # Then, we'll iterate through the letters and assign the first color to the first letter of the current consecutive group
    # and the second color to the last letter of the current consecutive group.
    # If we encounter a consecutive group of 1 letter, we'll assign the first color.
    # If we encounter a consecutive group of 2 letters, we'll assign the first color to the first letter and the second color to the second letter.
    # If we encounter a consecutive group of 3 or more letters, we'll assign the first color to the first letter and the second color to the last letter.
    # If we reach the end of the input string, we'll assign the first color to the last letter of the current consecutive group.

    ans = [None] * n

    i = 0
    while i < n:
        count = 1
        for j in range(i + 1, n):
            if s[j] != s[i]:
                break
            count += 1
        if count == 1:
            ans[i] = 0
        elif count == 2:
            ans[i] = 0
            ans[j - 1] = 1
        else:
            ans[i] = 0
            ans[j - 1] = 1
        i += count

    if ans[-1] is None:
        ans[-1] = 0

    print('YES')
    print(''.join(map(str, ans)))


if __name__ == '__main__':
    main()