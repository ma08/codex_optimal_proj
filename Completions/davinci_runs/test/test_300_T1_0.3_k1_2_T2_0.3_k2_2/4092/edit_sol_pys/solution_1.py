

def main():
    n = int(input()) #number of elements
    a = list(map(int, input().split())) #list of elements
    s = [0] * (n + 1) #list of sums
    for i in range(n): #summing up
        s[i + 1] = s[i] + a[i] 
    d = {} #dictionary of sums
    ans = 0 #maximal length of subarray
    for i in range(n + 1): #iterating through sums
        if s[i] in d: #if sum is in dictionary
            ans = max(ans, i - d[s[i]]) #update maximal length
        else: #if sum is not in dictionary
            d[s[i]] = i #add sum to dictionary
    print(n - ans) #print result

if __name__ == '__main__':
    main()
