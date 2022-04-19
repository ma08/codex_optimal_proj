

def min_length(n, words, k):
    for i in range(len(words)):
        if words[i] == k:
            return i

n = int(input())
k = input()
words = input().split()

print(min_length(n, words, k))
