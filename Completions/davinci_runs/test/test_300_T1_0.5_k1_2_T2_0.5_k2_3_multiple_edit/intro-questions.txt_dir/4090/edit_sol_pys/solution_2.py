

def min_length(n, words_):
    count = 1
    for i in range(n-1):
        if words_[i] != words_[i+1]:
            count += 1
    return count

n = int(input())
words_ = input().split()

print(min_length(n, words_))
