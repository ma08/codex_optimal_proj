

n = int(input())
s = input()

# first half of the string and its a and b counts
first_half = s[:n//2] 
a_count_first_half = first_half.count('a') 
b_count_first_half = first_half.count('b') 

# second half of the string and its a and b counts
second_half = s[n//2:] 
a_count_second_half = second_half.count('a') 
b_count_second_half = second_half.count('b') 

difference = abs(a_count_first_half - b_count_first_half) 
difference2 = abs(a_count_second_half - b_count_second_half) 

operations = min(difference, difference2) 

print(operations) 

if difference < difference2: 
    print(first_half + second_half) 
else:
    print(second_half + first_half) 
