


def main():
    n = int(input())
    text = input()
    print(min_length(text))


def min_length(text):
    words = text.split()
    dp = [0] * len(words)

    dp[0] = len(words[0])
    for i in range(1, len(words)):
        dp[i] = dp[i - 1] + len(words[i])

    for i in range(1, len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                if i > 0:
                    dp[j] = min(dp[j], dp[i - 1] + len(words[i]) + 1)
                else:
                    dp[j] = min(dp[j], len(words[i]) + 1)
    return dp[-1]

if __name__ == '__main__':
    main()