

def min_length(n, words):  # function to find the minimum length of the word
    count = 1
    for i in range(n - 1):
        if words[i] != words[i + 1]:
            count += 1
    return count


n = int(input())  # number of words
words = input().split()  # list of words

print(min_length(n, words))
