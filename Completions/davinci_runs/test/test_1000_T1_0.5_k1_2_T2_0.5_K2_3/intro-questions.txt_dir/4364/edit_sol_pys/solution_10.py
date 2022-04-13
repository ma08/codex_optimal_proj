

import re

# Get input
S = input()

# Check if input is valid
if len(S) != 4:
    print("NA1")
elif re.match("^\d{4}$", S) is None:
    print("NA2")
else:
    # Check if valid in YYMM format
    YY = int(S[:2])
    MM = int(S[2:])
    if YY < 1 or YY > 99:
        print("NA3")
    elif MM < 1 or MM > 12:
        print("NA4")
    else:
        # Check if valid in MMYY format
        if YY < 1 or YY > 99:
            print("MMYY")
        elif MM < 1 or MM > 12:
            print("YYMM")
        elif YY < 1 or YY > 99:
            print("MMYY")
        else:
            print("AMBIGUOUS")
