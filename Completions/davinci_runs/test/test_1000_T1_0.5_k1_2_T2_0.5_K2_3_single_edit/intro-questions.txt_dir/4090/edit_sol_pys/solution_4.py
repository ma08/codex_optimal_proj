

def min_length(n, words, k):
    if n%(k+1) == 0:
        return n//(k+1)
    else:
        return n//(k+1) + 1

n = int(input())
words = input().split()

k = int(input())

print(min_length(n, words, k))
