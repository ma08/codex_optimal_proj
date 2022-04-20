

#input
n = input().split()

#function
def is_good(n, a, b, c):
    if int(n[a])+int(n[b]) == int(n[c]):
        return True
    else:
        return False


#output
for i in range(len(n)):
    for j in range(i+1, len(n)):
        for k in range(j+1, len(n)):
            if is_good(n, i, j, k):
                print('Yes')
                exit()
print('No')
