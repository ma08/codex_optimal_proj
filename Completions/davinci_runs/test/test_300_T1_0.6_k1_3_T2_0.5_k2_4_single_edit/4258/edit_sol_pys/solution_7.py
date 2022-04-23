
import math

a, b, t = map(int, input().split())  # read a, b, t

ans = math.floor(t / a) * b  # calculate ans
print(int(ans))
