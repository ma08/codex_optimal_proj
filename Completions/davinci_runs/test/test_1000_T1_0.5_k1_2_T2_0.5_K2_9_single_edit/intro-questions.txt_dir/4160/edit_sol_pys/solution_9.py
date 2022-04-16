import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    # process line
    print(re.sub(r"\b([a-z]+) \1\b", r"\1", line))
