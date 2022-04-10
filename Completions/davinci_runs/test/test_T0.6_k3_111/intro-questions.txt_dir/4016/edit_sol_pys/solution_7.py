

from collections import Counter

def main():
    n, k = map(int, input().split()) # n = length of string, k = number of times to print
    t = input() # string

    c = Counter(t) # count all characters in string
    c = sorted(c.items(), key=lambda x: x[0]) # sort by character

    h = [] # temporary list
    for i in range(0, len(c), 2):
        h.append(c[i])
        h.append(c[i + 1])

    s = [] # list to store the final string
    for i in range(len(h)):
        s.append(h[i][0] * (n // 2))

    for i in h[::-1]: # reverse the list
        s.append(i[0] * (n // 2))

    s = "".join(s)

    if k == 1: # if k = 1, just print the string
        print(t)
    elif k == 2: # if k = 2, print the string once
        print(s)
    else: # if k > 2, print the string once, then print the string k - 2 times, then print the first n characters of the string
        print(s * (k - 2) + s[:n])

main()
