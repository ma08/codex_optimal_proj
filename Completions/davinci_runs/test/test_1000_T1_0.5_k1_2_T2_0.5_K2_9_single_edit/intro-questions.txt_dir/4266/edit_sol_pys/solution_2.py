

import numpy as np
import sys

k, x = map(int, input().split())

if k * 500 >= x:
    print('Yes')
else:
    print('No')
