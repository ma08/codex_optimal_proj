
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
a,b,c = map(int, input().split())
print("YES" if math.sqrt((a-b)**2+(b-c)**2+(c-a)**2)==a+b+c else "NO")
