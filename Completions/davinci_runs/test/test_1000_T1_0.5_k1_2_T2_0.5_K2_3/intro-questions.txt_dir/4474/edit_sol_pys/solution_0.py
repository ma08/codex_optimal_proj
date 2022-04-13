

# Python3 program to find the smallest good number 
def good(n): 
	
	# To store the result 
	res = n 
	
	# To store the sum of digits 
	s = sumOfDigits(n) 
	
	# Loop until we get a good number 
	while (s % 4 != 0): 
		
		# Increment the number 
		res += 1
		
		# Update the sum 
		s = sumOfDigits(res) 
	
	return res 
	
# Function to return the sum of digits in a number 
def sumOfDigits(n): 
	
	# To store the sum of digits 
	s = 0
	
	# Loop until n becomes 0 
	while (n > 0): 
		
		# Add last digit to the sum 
		s += n % 10
		
		# Remove the last digit 
		n = n // 10
	
	return s 
# greater than or equal to n. 


# Driver code 
if __name__ == "__main__" : 
	
	n = int(input())
	print(good(n))
