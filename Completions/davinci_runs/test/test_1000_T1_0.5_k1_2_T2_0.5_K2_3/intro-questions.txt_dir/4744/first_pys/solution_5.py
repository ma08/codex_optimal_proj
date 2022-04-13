

import math

V = int(input())

# Brute force solution
# for a in range(1, V+1):
#     for b in range(1, V+1):
#         for c in range(1, V+1):
#             if a*b*c == V:
#                 print(2*(a*b + a*c + b*c))
#                 break

# Solve equation V = a*b*c
# a = V^(1/3)
# b = V^(1/3)
# c = V^(1/3)

# Solve equation 2*(a*b + a*c + b*c)
# 2*(a*b + a*c + b*c) = 2*(a^2*b + a*c^2 + b^2*c)
# 2*(a*b + a*c + b*c) = 2*(a^2*V^(1/3) + a*V^(1/3)^2 + V^(1/3)*b^2)
# 2*(a*b + a*c + b*c) = 2*(a^2*V^(1/3) + a*V^(1/3)^2 + V^(1/3)*V^(2/3))
# 2*(a*b + a*c + b*c) = 2*(a^2*V^(1/3) + a*V^(1/3)^2 + V^(1/3)*V^(2/3))
# 2*(a*b + a*c + b*c) = 2*(a^2*V^(1/3) + a*V^(1/3)^2 + V^(1/3)*V^(2/3))
# 2*(a*b + a*c + b*c) = 2*(a^2*V^(1/3) + a*V^(1/3)^2 + V^(1/3)*V^(2/3))

print(2*(math.pow(V, (1/3))**2 + math.pow(V, (1/3))**2 + math.pow(V, (1/3))**2))