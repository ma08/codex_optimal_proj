

# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''

# Snowy Winter
# Inputs number of years, and number of days between the end of summer and first day of snow
# Outputs number of years that it had never snowed this early
def snowy_winter(n, d_m, d_m_less):
	d_m_less = int(input())
	count = 0
	for i in range(n):
		d_m_less = int(input())
		if d_m_less > d_m:
			count += 1
	return count

# Gets user input
n, d_m, d_m_less = map(int, input().split())

# Output, prints number of years it had never snowed this early
print("It hadn't snowed this early in", snowy_winter(n, d_m, d_m_less), "years!")
