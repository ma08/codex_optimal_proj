

# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''

# Snowy Winter
# Input number of years, and number of days between end of summer and first day of snow for the current year
# Output number of years that it had never snowed this early
def snowy_winter(n, d_m_curr):
	d_m_less = int(input()) # Number of days between end of summer and first day of snow for the previous year
	count = 0
	for i in range(n-1):
		d_m_less = int(input())
		if d_m_less > d_m:
			count += 1
	return count

# Gets user input
n, d_m = map(int, input().split())

# Output, prints number of years it had never snowed this early
print("It hadn't snowed this early in", snowy_winter(n, d_m), "years!")
