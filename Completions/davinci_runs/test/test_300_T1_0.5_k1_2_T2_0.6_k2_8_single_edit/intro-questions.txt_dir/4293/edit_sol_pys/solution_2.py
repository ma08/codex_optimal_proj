# -*- coding: utf-8 -*-

import os
import math
import numpy as np
from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
import sys

def main():
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))

if __name__ == "__main__":
    main()
