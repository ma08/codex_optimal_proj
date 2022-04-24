n = int(input())
words = input().split()

def min_length(n, words):
    count = 1
    for i in range(n-1):
        if words[i] != words[i+1]:
            count += 1
    return count

print(min_length(n, words))
