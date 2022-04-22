


def min_length(n, words):
    count = 0
    for i in range(n - 1):
        if words[i] != words[i + 1]:
            count = count + 1

    return count

n = int(input())
words = input().split()
print(min_length(n, words))
