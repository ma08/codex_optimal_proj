

"""
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""
 
# Write your code here
x = int(input()) # Reading input from STDIN
y = int(input()) # Reading input from STDIN
z = int(input()) # Reading input from STDIN
n = int(input()) # Reading input from STDIN
 
l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(l)
