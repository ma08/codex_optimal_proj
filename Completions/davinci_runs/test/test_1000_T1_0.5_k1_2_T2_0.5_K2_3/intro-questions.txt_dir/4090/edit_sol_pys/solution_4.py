

def min_length(n, words):
    counter = 1
    for i in range(n - 1):
        if words[i] != words[i+1]:
            counter += 1
    return counter

n = int(input())
words = input().split()

print(min_length(n, words))
