

#!/bin/python3

import math
import os
import random
import re
import sys

while len(a) > 1:
    a.sort()
    attacker = random.randint(0, len(a)-1)
    victim = random.randint(0, len(a)-1)
    if a[attacker] > a[victim]:
        a[victim] = 0
        a = [i for i in a if i != 0]
    else:
        a[attacker] = 0
        a = [i for i in a if i != 0]
print(a[0])
