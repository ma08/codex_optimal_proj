

def min_length(n, words):  # n is the number of words
    count = 1
    for i in range(n - 1):
        if words[i] != words[i + 1]:  # compare the current word and the next word
            count += 1

    return count

n = int(input())
words = input().split()

print(min_length(n, words))
