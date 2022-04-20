

def min_length(n, words, k):
    # count = 1
    # for i in range(n-1):
    #     if words[i] != words[i+1]:
    #         count += 1
    # return count
    if k == 0:
        return n
    elif n == 1:
        return n
    else:
        if words[0] == words[1]:
            return min_length(n-1, words[1:], k)
        else:
            return min_length(n-1, words[1:], k-1)

n = int(input())
k = int(input())
words = input().split()

print(min_length(n, words, k))
