

import math
n = int(input())

ans = 10**10
for i in range(1,int(math.sqrt(n))+1):
	if n % i == 0:
		a = i
		b = n // i
		ans = min(ans,len(str(a)),len(str(b)))

print(ans)