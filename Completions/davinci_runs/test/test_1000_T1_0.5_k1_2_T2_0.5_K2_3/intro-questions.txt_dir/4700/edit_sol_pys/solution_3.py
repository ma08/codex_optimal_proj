

n,m = [int(i) for i in input().split()]

h = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

#print(n)
#print(m)
#print(h)
#print(a)



# returns the index of the first occurence of the value in the array
def find(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1




def solve(n,m,h,a):
    #print("n,m,h,a:",n,m,h,a)
    if len(h) == 1 and len(a) == 1:
        if h[0] == a[0]:
            return 1
        else:
            return 0
    elif len(h) == 1 and len(a) > 1:
        for i in range(len(a)):
            if h[0] == a[i]:
                return i+1
        return 0
    elif len(h) > 1 and len(a) == 1:
        for i in range(len(h)):
            if a[0] == h[i]:
                return i+1
        return 0
    else:
        i = find(h,a[0])
        #print("i:",i)
        if i == -1:
            return 0
        elif i == 0:
            return solve(n,m,h[1:],a[1:])
        elif i == len(h)-1:
            return solve(n,m,h[:i],a[:i])
        else:
            return solve(n,m,h[:i],a[:i]) + solve(n,m,h[i+1:],a[i+1:])




print(solve(n,m,h,a))
