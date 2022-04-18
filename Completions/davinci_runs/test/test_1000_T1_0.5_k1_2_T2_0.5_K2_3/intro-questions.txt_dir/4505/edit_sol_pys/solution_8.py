
S = list(input())

for i in range(len(S)):
    if S[i] == 'a':
        continue
    elif S[i] == 'b':
        if i == len(S) - 1:
            print('Yes')
            exit()
        elif S[i+1] == 'c':
            continue
        else:
            print('No')
            exit()
    elif S[i] == 'c':
        if i == len(S) - 1 or i == 0:
            print('No')
            exit()
        elif S[i-1] == 'a' and S[i+1] == 'b':
            continue
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()
print('Yes')
