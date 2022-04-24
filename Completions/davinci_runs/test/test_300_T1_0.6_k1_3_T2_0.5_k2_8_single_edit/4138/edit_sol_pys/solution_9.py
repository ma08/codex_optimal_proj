

#-----Solution-----
#The following steps are used to solve the problem
#1. Find the block number of the digit
#2. Find the position of the digit in the block
#3. Calculate the value of the digit

#1. Finding the block number of the digit
#The block number $b$ of the digit is the number of elements in the sequence before the digit.
#For example, the block number of the digit at the position 40 is 40.
#i.e. $b$ is equal to the number of digits in the sequence before the digit,
#which is equal to the number of digits in the first $b$ blocks.

#The number of elements in the first $b$ blocks is given by the following formula:
#$$\sum_{i=1}^b i = \frac{b(b+1)}{2}$$

#For example, if $b=40$, then the number of elements in the first $40$ blocks is
#$$\frac{40(40+1)}{2} = 820$$

#Therefore, to find the block number of the digit at the position $k$, we can solve the following equation:
#$$\frac{(b)(b+1)}{2} = k$$

#Since $k$ is a positive integer, $b$ must be an integer.
#The solutions to the equation are:
#$$b = \frac{-1 + \sqrt{8k+1}}{2}$$ or $$b = \frac{-1 - \sqrt{8k+1}}{2}$$
#or
#$$b = \frac{-1 - \sqrt{8k+1}}{2}$$

#The solution $b = \frac{-1 + \sqrt{8k+1}}{2}$ is not an integer if $k$ is not a square number.
#So we can ignore it.

#The solution $b = \frac{-1 - \sqrt{8k+1}}{2}$ is an integer if $k$ is a square number.
#If $k$ is not a square number, then the solution is not an integer.
#In this case, we can round down the solution to the nearest integer.

#The following function finds the block number of the digit at the position $k$
def find_block_number(k):
    return int((-1 - (8*k + 1)**0.5)/2)

#2. Finding the position of the digit in the block
#The position $p$ of the digit in the block is the number of digits in the sequence before the block.
#For example, the position of the digit at the position 40 is 36.
#i.e. $p$ is equal to the number of digits in the sequence before the block,
#which is equal to the number of digits in the first $b-1$ blocks.

#The number of elements in the first $b-1$ blocks is given by the following formula:
#$$\sum_{i=1}^{b-1} i = \frac{(b-1)(b)}{2}$$

#Therefore, to find the position of the digit in the block, we can solve the following equation:
#$$\frac{(b-1)(b)}{2} = p$$

#The solutions to the equation are:
#$$p = \frac{b(b-1)}{2}$$

#The following function finds the position of the digit in the block
def find_position(b):
    return int(b*(b-1)/2)

#3. Calculating the value of the digit
#The value $d$ of the digit is the number of digits in the block before the digit.
#For example, the value of the digit at the position 40 is 4.
#i.e. $d$ is equal to the number of digits in the block before the digit,
#which is equal to the number of digits in the first $p$ blocks before the block.

#The number of elements in the first $p$ blocks before the block is given by the following formula:
#$$\sum_{i=1}^p i = \frac{p(p+1)}{2}$$

#Therefore, to find the value of the digit, we can solve the following equation:
#$$\frac{p(p+1)}{2} = d$$

#The solutions to the equation are:
#$$d = \frac{p(p+1)}{2}$$

#The following function finds the value of the digit
def find_digit(p):
    return int(p*(p+1)/2)


#4. Finding the digit at the position $k$
#The digit at the position $k$ is the digit in the block at the position $d$ from the left.
#For example, the digit at the position 40 is the digit at the position 4 from the left in the block at the position 36.

#The digit at the position $d$ from the left in the block is the $d$-th digit in the block.
#The block is the sequence of all numbers from $1$ to $b$.
#The $d$-th digit in the block is the $d$-th digit in the sequence of all numbers from $1$ to $b$.

#The following function finds the digit at the position $k$
def find_digit_at_position(k):
    #1. Find the block number of the digit
    b = find_block_number(k)
    #2. Find the position of the digit in the block
    p = find_position(b)
    #3. Calculate the value of the digit
    d = find_digit(p)
    #4. Find the digit at the position $k$
    return int(str(b)[d-1])

#-----Testing-----
q = int(input())
for i in range(q):
    k = int(input())
    print(find_digit_at_position(k))
