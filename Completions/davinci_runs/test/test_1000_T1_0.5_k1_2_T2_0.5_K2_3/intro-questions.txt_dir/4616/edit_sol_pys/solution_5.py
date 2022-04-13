

import sys

# Get the input
s = sys.stdin.readline().rstrip()

# Abbreviate the string by replacing the middle characters
i18n = s[0]
for i in range(1, len(s)-2):
    if i < (len(s)-2):
        i18n += str(len(s)-i-2)
    else:
        i18n += s[i]
i18n += s[-1]

# Print the output
print(i18n)
