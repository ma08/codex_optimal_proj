

s = input()

s_sum = sum([int(x) for x in s])

if s_sum % 3 == 0:
    print(len(s)-1)
else:
    s_sum = [int(x) for x in s]
    cuts = 0
    for i in range(len(s_sum)):
        if s_sum[i] % 3 == s_sum % 3:
            s_sum = s_sum[:i]+s_sum[i+1:]
            cuts += 1
            break
    if cuts == 0:
        print(0)
    else:
        print(cuts+len(s_sum)-1)