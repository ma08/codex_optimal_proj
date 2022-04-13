import numpy as np

n = int(input())
ans = input().split()

ans = [float(ans[i]) for i in range(len(ans)) if i != n-1]
ans = np.array(ans)

print(len(ans))
