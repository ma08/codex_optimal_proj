
K = int(input())  # max length of the output
S = input()  # input string

if len(S) > K:
    print(S[:K] + '...')  # if length of the input string is longer than max length, print the first K characters with '...'
else:
    print(S)  # if length of the input string is shorter than max length, print the string.
