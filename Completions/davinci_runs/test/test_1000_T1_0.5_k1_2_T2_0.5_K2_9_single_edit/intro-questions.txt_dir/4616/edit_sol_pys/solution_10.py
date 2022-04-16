

import sys

# Get the input and remove the newline
s = sys.stdin.readline()
s = s.rstrip()

# Abbreviate the string
i18n = s[0:1]
for i in range(1, len(s)-2):
    if i < (len(s)-2):
        i18n += str(len(s)-i-2) + s[i:i+1]
    else:
        i18n += s[i:i+1]
i18n += s[-1:]

# Print the output
print(i18n)
