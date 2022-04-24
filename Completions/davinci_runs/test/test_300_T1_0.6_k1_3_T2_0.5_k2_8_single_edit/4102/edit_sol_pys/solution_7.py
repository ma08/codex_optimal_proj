

#input
n = input()

#function
def is_good(n):
    for i in range(len(n)-2):
        for j in range(i+1, len(n)-1):
            for k in range(j+1, len(n)): 
                if int(n[i])+int(n[j]) == int(n[k]): 
                    return True
    return False


#output
if is_good(n):
    print('Yes')
else:
    print('No')
