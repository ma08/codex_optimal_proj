

def min_length(words):
    count = 1
    for i in range(n-1):
        if words[i] != words[i+1]:
            count += 1
    return count

n = int(input())
words = input().split()

print(min_length(n, words))
