
S = input()

S = list(S)
S.sort()

# print(S)

for i in range(len(S) - 1):
    if ord(S[i]) + 1 < ord(S[i + 1]):
        if ord(S[i]) + 1 == ord('a') + 26:
            print('None')
            break
        else:
            print(chr(ord(S[i]) + 1))
            break
    elif i == len(S) - 2:
        if ord(S[i + 1]) + 1 == ord('a') + 26:
            print('None')
            break
        else:
            print(chr(ord(S[i + 1]) + 1))
            break
