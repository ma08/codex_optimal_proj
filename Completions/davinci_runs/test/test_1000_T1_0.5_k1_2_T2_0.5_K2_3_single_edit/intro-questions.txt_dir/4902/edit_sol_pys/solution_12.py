

#-----Solution-----
#-----Solution-----


import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'(?<=[^\s])[.,]', '', line))
