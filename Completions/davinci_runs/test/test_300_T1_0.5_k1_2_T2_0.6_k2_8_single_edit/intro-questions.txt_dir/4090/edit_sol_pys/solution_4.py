
def min_length(n, words):
    count = 1
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            count += 1
        # print(count)
    return count - 1


n = int(input())
words = input().split()

print(min_length(n, words))
