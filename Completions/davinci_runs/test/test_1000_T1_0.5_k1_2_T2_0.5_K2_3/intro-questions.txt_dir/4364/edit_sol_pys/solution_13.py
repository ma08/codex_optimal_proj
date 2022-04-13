
import re

# Get input
S = input()

# Check if input is valid
if len(S) != 4:
    print("NA")
elif re.match("^\d{4}$", S) is None:
    print("NA")
else:
    # Check if valid in YYMM formate
    YY = int(S[:2])
    MM = int(S[2:])
    if YY < 1 or YY > 99:
        print("NA")
    elif MM < 1 or MM > 12:
        print("NA")
    else:
        # Check if valid in MMYY formate
        if MM < 1 or MM > 12:
            print("YYMM")
        elif YY < 1 or YY > 99:
            print("MMYY")
        else:
            print("AMBIGUOUS")
