

def isSubsequence(string, sub):
    if(len(sub)==0):
        return True
    
    i = 0
    j = 0
    
    while(i<len(string) and j<len(sub)):
        if string[i] == sub[j]:
            j+=1
        i+=1
    
    return j == len(sub)

def subsequence(string, k):
    if(len(string)<k):
        return -1
    
    subs = []
    for i in range(1, len(string)+1):
        for j in range(0, len(string)-i+1):
            subs.append(string[j:j+i])
    
    subs = list(set(subs))
    subs.sort(key=len)
    subs.reverse()
    print(subs)
    
    for i in range(0, len(subs)):
        for j in range(i+1, len(subs)):
            if(isSubsequence(subs[i], subs[j])):
                del subs[j]
                break
    
    print(subs)
    
    if(len(subs)<k):
        return -1
    else:
        return sum([len(string)-len(sub) for sub in subs[:k]])

n, k = [int(x) for x in input().split()]
string = input()

print(subsequence(string, k))