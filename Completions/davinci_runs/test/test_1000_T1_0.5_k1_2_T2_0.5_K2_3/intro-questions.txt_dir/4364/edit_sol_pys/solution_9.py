
import re

# Get input
S = input()

# Check if input is valid
if len(S) != 4:
    print("NA")
elif re.match("^\d{4}$", S) is None:
    print("NA")
else:
    # Check if valid in YYMM format and MMYY format
    if 1 <= int(S[:2]) <= 99 and 1 <= int(S[2:]) <= 12:
        print("YYMM")
    elif 1 <= int(S[2:]) <= 99 and 1 <= int(S[:2]) <= 12:
        print("MMYY")
    elif 1 <= int(S[:2]) <= 99 and 1 <= int(S[2:]) <= 12:
        print("AMBIGUOUS")
    else: print("NA")
