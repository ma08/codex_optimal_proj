
# The solution to this problem is really simple
s = input()

# If the string contains two consecutive occurrences of the letter s, then output hiss,
# otherwise, output no hiss.
print("hiss" if "ss" in s else "no hiss")
