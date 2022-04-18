import sys
from collections import Counter
print(Counter(sys.stdin.readlines()).most_common()[0][0])
