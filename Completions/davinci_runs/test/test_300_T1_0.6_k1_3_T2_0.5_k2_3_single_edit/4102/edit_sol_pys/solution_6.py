

#input
n = input() # n = '123'

#function
def is_good(n): # n = '123'
    for i in range(len(n)): # i = 0
        for j in range(i+1, len(n)): # j = 1, 2
            for k in range(j+1, len(n)): # k = 2
                if int(n[i])+int(n[j]) == int(n[k]): # 1 + 2 == 3
                    return True
    return False


#output
if is_good(n): # True
    print('Yes')
else:
    print('No')
