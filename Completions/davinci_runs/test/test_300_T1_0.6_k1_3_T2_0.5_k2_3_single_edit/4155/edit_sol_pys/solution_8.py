

import math
import numpy as np

N, M = map(int, input().split())
x_list = list(map(int, input().split()))

x_list.sort()

diff_list = [x_list[i+1]-x_list[i] for i in range(M-1)]
diff_list.sort()

if M > N:
    print(sum(diff_list[:(M-N)]))
else:
    print(0)
