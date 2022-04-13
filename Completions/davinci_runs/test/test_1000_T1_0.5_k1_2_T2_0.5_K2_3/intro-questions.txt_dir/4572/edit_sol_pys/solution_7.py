S = input()
S = list(S)

S.sort()

for i in range(len(S) - 1):
    if ord(S[i]) + 1 == ord(S[i + 1]):
        if i == len(S) - 2:
            print(chr(ord(S[i + 1]) + 1))
        else:
            continue
    else:
        print(chr(ord(S[i]) + 1))
        break
