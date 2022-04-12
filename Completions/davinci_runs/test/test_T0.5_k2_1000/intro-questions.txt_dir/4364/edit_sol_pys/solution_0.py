
import re

# Get input
S = input().strip()

# Check if input is valid
if len(S) != 4:
    print("NA", end="")
elif re.match("^\d{4}$", S) is None:
    print("NA", end="")
else:
    # Check if valid in YYMM format
    YY = int(S[:2])
    MM = int(S[2:])
    if YY < 1 or YY > 99:
        print("NA", end="")
    elif MM < 1 or MM > 12:
        print("NA", end="")
    else:
        # Check if valid in MMYY format 
        if MM < 1 or MM > 12:
            print("YYMM", end="")
        elif YY < 1 or YY > 99:
            print("MMYY", end="")
        else:
            print("AMBIGUOUS", end="")
