

def main():
    n, k = map(int, input().split())  # n is the number of characters in the string, k is the number of distinct characters in the string
    s = input()  # the string

    if k > (1 << n) - 1:  # if k is greater than the number of possible distinct characters in the string, print -1
        print(-1)
        return

    s = [c for c in s]  # convert the string to a list of characters
    s.sort()  # sort the list of characters
    s = "".join(s)  # convert the list of characters back to a string
    print(s)  # print the sorted string

    curr = s[0]  # the current character
    prev = s[0]  # the previous character
    res = 0  # the number of distinct characters in the string
    i = 1  # the index of the current character
    while i < len(s):  # iterate through the string
        if s[i] != prev:  # if the current character is not the same as the previous character
            res += len(curr)  # add the length of the current character to the number of distinct characters
            curr = ""  # reset the current character
        prev = s[i]  # update the previous character
        curr += s[i]  # update the current character
        i += 1  # update the index of the current character
    res += len(curr)  # add the length of the current character to the number of distinct characters

    print(res)  # print the number of distinct characters in the string

main()
