N = int(input())
S = input()
K = int(input())


for i in range(len(S)):
    if S[i].isalpha():
        print(chr(ord(S[i]) + K), end='')
    else:
        print(S[i], end='')
