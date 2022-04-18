

def min_length(n, words):  # min_length is a function that returns the minimum length of the string
    count = 1
    for i in range(n-1):  # range(n-1) is a range from 0 to n-1
        if words[i] != words[i+1]:
            count += 1  # count is a variable that counts the number of words in the string
    return count


n = int(input())  # n is the number of words in the string
words = input().split()  # words is a list of the words in the string

print(min_length(n, words))
