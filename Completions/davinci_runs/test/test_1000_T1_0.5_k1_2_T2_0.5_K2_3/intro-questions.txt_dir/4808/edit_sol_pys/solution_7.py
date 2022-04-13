

# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''
n, d_m = map(int, input().split())
# Snowy Winter
# Inputs: number of years, and number of days between end of summer and first day of snow
# Outputs: number of years that it had never snowed this early
d_m_less = int(input())
count = 0
for i in range(n-1):
	d_m_less = int(input())
	if d_m_less > d_m:
		count += 1

print("It hadn't snowed this early in", count, "years!")
