

def min_length(n, words):
    min_len = n
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                if j-i < min_len:
                    min_len = j-i
    return min_len

n = int(input())
words = input().split()

print(min_length(n, words))
