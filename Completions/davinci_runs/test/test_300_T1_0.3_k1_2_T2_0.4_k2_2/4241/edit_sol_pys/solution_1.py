
import sys

def main():
    s = sys.stdin.readline().rstrip() #input string
    t = sys.stdin.readline().rstrip() #input string
    print(min_changes(s, t)) #print the output

def min_changes(s, t):
    """
    Returns the minimum number of characters in s that need to be changed
    to make t a substring of s.
    """
    # Create a list of indices of the characters in s that match the first character in t.
    indices = [i for i, c in enumerate(s) if c == t[0]] #list of indices of character in s that match the first character in t
    # If there are no characters in s that match the first character in t, then we need to change len(s) characters.
    if not indices: #if there are no characters in s that match the first character in t
        return len(s) #return the length of s
    # If there are characters in s that match the first character in t, then we need to check if t is a substring of s starting at each index in indices.
    else: #if there are characters in s that match the first character in t
        for i in indices: #for each index in indices
            # If t is a substring of s starting at index i, then we need to change i characters.
            if is_substring(s, t, i): #if t is a substring of s starting at index i
                return i #return i
        # If t is not a substring of s starting at any index in indices, then we need to change len(s) - indices[-1] characters.
        return len(s) - indices[-1] #return the length of s - the last index in indices

def is_substring(s, t, i):
    """
    Returns True if t is a substring of s starting at index i,
    otherwise returns False.
    """
    # If the length of s starting at index i is less than the length of t, then t cannot be a substring of s starting at index i.
    if len(s) - i < len(t): #if the length of s starting at index i is less than the length of t
        return False #return False
    # If the length of s starting at index i is greater than or equal to the length of t, then check if the characters in s starting at index i match the characters in t.
    else: #if the length of s starting at index i is greater than or equal to the length of t
        for j in range(len(t)): #for each character in t
            if s[i + j] != t[j]: #if the character in s starting at index i + j is not equal to the character in t at index j
                return False #return False
        return True #return True

if __name__ == '__main__':
    main()
