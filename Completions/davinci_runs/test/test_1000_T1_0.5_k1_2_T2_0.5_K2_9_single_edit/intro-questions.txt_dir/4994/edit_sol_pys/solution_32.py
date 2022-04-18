#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:57:46 2019

@author: carl
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:57:46 2019

@author: carl
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:53:45 2019

@author: carl
"""

# Read input
xy = []
for i in range(3):
    xy.append([int(i) for i in input().split()])

# Find the missing point
for i in range(3):
    for j in range(3):
        if xy[i][0] == xy[j][0] and xy[i][1] != xy[j][1]:
            x = xy[i][0]
            y = xy[i][1] + xy[j][1] - xy[i][1]
        elif xy[i][1] == xy[j][1] and xy[i][0] != xy[j][0]:
            x = xy[i][0] + xy[j][0] - xy[i][0]
            y = xy[i][1]
        if x and y:
            print(x, y)
            break
    if x and y:
        break
