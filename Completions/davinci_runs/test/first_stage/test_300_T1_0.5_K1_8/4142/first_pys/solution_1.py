

S = input()

odd_num = [R,U,D]
even_num = [L,U,D]

if S[0] in odd_num:
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] not in odd_num:
                print('No')
                exit()
        else:
            if S[i] not in even_num:
                print('No')
                exit()
    print('Yes')
else:
    print('No')