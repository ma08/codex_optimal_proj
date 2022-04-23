

def findLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 1

    # the stack keeps the index of the characters
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
            else:
                if s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

    if len(stack) == 0:
        return len(s)

    max_length = 0
    end = len(s)
    while len(stack) > 0:
        start = stack.pop()
        max_length = max(max_length, end - start - 1)
        end = start
    max_length = max(max_length, end)

    return max_length


if __name__ == "__main__":
    s = raw_input()
    print findLongestSubstring(s)
