


def min_length(n, words, k):
    count = 1
    for i in range(n - 1):
        if words[i][k] != words[i + 1][k]:
            count += 1

    return count

n = int(input())
words = input().split()

print(min_length(n, words, k))
