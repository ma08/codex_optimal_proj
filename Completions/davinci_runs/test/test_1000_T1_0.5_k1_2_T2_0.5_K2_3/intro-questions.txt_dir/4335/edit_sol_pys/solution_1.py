


def is_palindrome(s):
    # First, get the length of the string, n.
    # Second, get the string, s.
    n = int(input())
    s = input()

    # If n is even, check if s[:n//2] is equal to s[(n//2):].
    # If n is odd, check if s[:n//2] is equal to s[(n//2)+1:].
    # If either of the above conditions is true, print "Yes".
    # Otherwise, print "No".
    if n % 2 == 0:
        if s[:n//2] == s[(n//2):]:
            print("Yes")
        else:
            print("No")
    else:
        if s[:n//2] == s[(n//2)+1:]:
            print("Yes")
        else:
            print("No")

is_palindrome()
