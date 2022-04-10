

n = int(input())
s = input()

def solution(s):
    if len(s) == 3:
        return "012"
    if len(s) == 6:
        return "001122"
    
    #find the first instance of 011
    for i in range(len(s) - 2):
        if s[i:i+3] == "011":
            break
        
    #find the first instance of 001 after the first 011
    for j in range(i + 1, len(s) - 2):
        if s[j:j+3] == "001":
            break
        
    #find the first instance of 012 after the first 001
    for k in range(j + 1, len(s) - 2):
        if s[k:k+3] == "012":
            break
        
    #find the first instance of 020 after the first 012
    for l in range(k + 1, len(s) - 2):
        if s[l:l+3] == "020":
            break
        
    #construct the string between the first 011 and the first 020
    string = s[:i] + "012"
    string += "0" * (j - i - 1)
    string += "012"
    string += "0" * (k - j - 1)
    string += "012"
    string += "0" * (l - k - 1)
    string += "020"
    string += s[l + 3:]
    
    return string
    
print(solution(s))