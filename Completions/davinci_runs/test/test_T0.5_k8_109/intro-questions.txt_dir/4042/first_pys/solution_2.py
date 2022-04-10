

#The solution is a simple math problem.

def main():
	x = float(input())
	#First, find the integer part of x.
	a = int(x)
	#Subtract the integer part from x to get the decimal part.
	b = x - a
	#Multiply the decimal part by 100 to get the fractional part, then round it to the nearest integer.
	c = int(round(b * 100))
	#Print the solution.
	print(a, c)

if __name__ == '__main__':
	main()