#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:35:45 2020

@author: jinlingxing
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:34:07 2020

@author: jinlingxing
"""


n = int(input())
a = list(map(int, input().split()))

l = [0] * n

for i in range(n):
    l[a[i]-1] = i+1

for i in range(n):
    if i == n-1:
        print(l[i])
    else:
        print(l[i], end=' ')
