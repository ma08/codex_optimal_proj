

def min_length(n, words, k):
    for i in range(n):
        if words[i] == k:
            return i

n = int(input())
words = input().split()

print(min_length(n, words))
