

S = input()

def isPalindrome(S):
    for i in range(int(len(S)/2)):
        if S[i] != S[len(S)-i-1]:
            return False
    return True

def minHugs(S):
    if isPalindrome(S):
        return 0
    else:
        for i in range(int(len(S)/2)):
            if S[i] != S[len(S)-i-1]:
                return min(minHugs(S[:i]+S[len(S)-i-1]+S[i+1:]), minHugs(S[:len(S)-i-1]+S[i]+S[len(S)-i:]))+1
        return 1

print(minHugs(S))