

def min_length(n, word):
    count = 1
    for i in range(n - 1):
        if word[i] != word[i + 1]:
            count += 1

    return count

n = int(input())
word = input().split()

print(min_length(n, word) - 1)
