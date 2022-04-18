
# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''

# Snowy Winter
# Inputs number of years, and number of days between end of summer and first day of snow, then the number of days between the end of summer and the first day of snow
# Outputs number of years that it had never snowed this early, and the number of years that it had snowed this early
def snowy_winter(n, d_m, d_m_less):
	count_more = 0
	count_less = 0
	for i in range(n):
		if d_m_less > d_m:
			count_more += 1
		else:
			count_less += 1
		d_m_less = int(input())
	return count_more, count_less

# Gets user input
n, d_m = map(int, input().split())
d_m_less = int(input())

# Output, prints number of years it had never snowed this early, and the number of years that it had snowed this early
count_more, count_less = snowy_winter(n, d_m, d_m_less)
print("It hadn't snowed this early in", count_more, "years!")
print("It had snowed this early in", count_less, "years!")
