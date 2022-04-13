def get_beautiful_substring(s, k): 
    if len(s) == 1: 
        return len(s) 
    if len(set(s)) == 1: 
        return len(s) 
    max_len = 1 
    for i in range(len(s)): 
        for j in range(len(s)-1, i, -1): 
            if len(set(s[i:j+1])) == 1: 
                if (j-i+1)%k == 0: 
                    max_len = max(j-i+1, max_len) 
    return max_len 
  
T = int(input()) 
for _ in range(T): 
    n, k = map(int, input().split()) 
    s = input() 
    print(get_beautiful_substring(s, k)) 
