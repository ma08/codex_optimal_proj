

# SOLUTION
# This is a greedy problem.
# We can start from the middle of the array and continue to fill the array
# with the maximum possible number of elements.

# We will use a function to calculate the maximum possible sum of absolute
# differences between adjacent numbers in the array
# for a given number of elements and a given sum.

# This function will return the maximum possible sum of absolute
# differences between adjacent numbers in the array
# for a given number of elements and a given sum.
# The array will be filled with the maximum possible number of elements
# starting from the middle.
def max_sum_of_absolute_differences(n, m):
    
    # If n is odd, the middle element will be the maximum possible number,
    # which is m divided by n.
    # If n is even, the middle element will be the maximum possible number,
    # which is m divided by n, minus one.
    # We will use this middle element to start filling the array.
    if n % 2 == 1:
        middle_element = m // n
    else:
        middle_element = m // n - 1
    
    # We will use a variable to keep track of the sum of the array.
    # We will use this variable to check if we can add another element
    # to the array.
    sum_of_array = middle_element
    
    # We will use a variable to keep track of the sum of absolute
    # differences between adjacent numbers in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    sum_of_absolute_differences = 0
    
    # We will use a variable to keep track of the current element.
    # We will use this variable to check if we can add another element
    # to the array.
    current_element = middle_element
    
    # We will use a variable to keep track of the number of elements
    # in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    number_of_elements = 1
    
    # We will use a variable to keep track of the maximum possible number
    # of elements in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    max_number_of_elements = n // 2
    
    # We will use a variable to keep track of the number of elements
    # in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    number_of_elements_after_middle = 0
    
    # We will use a variable to keep track of the maximum possible number
    # of elements in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    max_number_of_elements_after_middle = n // 2
    
    # We will use a variable to keep track of the maximum possible number
    # of elements in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    max_number_of_elements_before_middle = n // 2
    
    # We will use a variable to keep track of the number of elements
    # in the array.
    # We will use this variable to check if we can add another element
    # to the array.
    number_of_elements_before_middle = 0
    
    # We will use a while loop to fill the array with the maximum
    # possible number of elements.
    while True:
        
        # We will use an if statement to check if we can add another
        # element to the array before the middle element.
        if number_of_elements_before_middle < max_number_of_elements_before_middle:
            
            # We will use a nested if statement to check if we can add
            # another element to the array before the middle element.
            if current_element > 0 and current_element * number_of_elements + sum_of_array <= m:
                
                # We will add another element to the array before the
                # middle element.
                current_element -= 1
                
                # We will update the sum of the array.
                sum_of_array += current_element
                
                # We will update the sum of absolute differences between
                # adjacent numbers in the array.
                sum_of_absolute_differences += current_element
                
                # We will update the number of elements in the array.
                number_of_elements += 1
                
                # We will update the number of elements in the array
                # before the middle element.
                number_of_elements_before_middle += 1
                
                # We will update the number of elements in the array
                # after the middle element.
                number_of_elements_after_middle = number_of_elements - number_of_elements_before_middle - 1
        
        # We will use an if statement to check if we can add another
        # element to the array after the middle element.
        if number_of_elements_after_middle < max_number_of_elements_after_middle:
            
            # We will use a nested if statement to check if we can add
            # another element to the array after the middle element.
            if current_element * number_of_elements + sum_of_array <= m:
                
                # We will add another element to the array after the
                # middle element.
                current_element += 1
                
                # We will update the sum of the array.
                sum_of_array += current_element
                
                # We will update the sum of absolute differences between
                # adjacent numbers in the array.
                sum_of_absolute_differences += current_element
                
                # We will update the number of elements in the array.
                number_of_elements += 1
                
                # We will update the number of elements in the array
                # after the middle element.
                number_of_elements_after_middle += 1
                
                # We will update the number of elements in the array
                # before the middle element.
                number_of_elements_before_middle = number_of_elements - number_of_elements_after_middle - 1
        
        # We will use an if statement to check if we can add another
        # element to the array before the middle element.
        if number_of_elements_before_middle < max_number_of_elements_before_middle:
            
            # We will use a nested if statement to check if we can add
            # another element to the array before the middle element.
            if current_element > 0 and current_element * number_of_elements + sum_of_array <= m:
                
                # We will add another element to the array before the
                # middle element.
                current_element -= 1
                
                # We will update the sum of the array.
                sum_of_array += current_element
                
                # We will update the sum of absolute differences between
                # adjacent numbers in the array.
                sum_of_absolute_differences += current_element
                
                # We will update the number of elements in the array.
                number_of_elements += 1
                
                # We will update the number of elements in the array
                # before the middle element.
                number_of_elements_before_middle += 1
                
                # We will update the number of elements in the array
                # after the middle element.
                number_of_elements_after_middle = number_of_elements - number_of_elements_before_middle - 1
        
        # We will use an if statement to check if we can add another
        # element to the array after the middle element.
        if number_of_elements_after_middle < max_number_of_elements_after_middle:
            
            # We will use a nested if statement to check if we can add
            # another element to the array after the middle element.
            if current_element * number_of_elements + sum_of_array <= m:
                
                # We will add another element to the array after the
                # middle element.
                current_element += 1
                
                # We will update the sum of the array.
                sum_of_array += current_element
                
                # We will update the sum of absolute differences between
                # adjacent numbers in the array.
                sum_of_absolute_differences += current_element
                
                # We will update the number of elements in the array.
                number_of_elements += 1
                
                # We will update the number of elements in the array
                # after the middle element.
                number_of_elements_after_middle += 1
                
                # We will update the number of elements in the array
                # before the middle element.
                number_of_elements_before_middle = number_of_elements - number_of_elements_after_middle - 1
        
        # We will use an if statement to check if we cannot add another
        # element to the array.
        if (number_of_elements_after_middle == max_number_of_elements_after_middle and
            number_of_elements_before_middle == max_number_of_elements_before_middle):
            
            # We will break out of the while loop.
            break
    
    # We will return the maximum possible sum of absolute differences
    # between adjacent numbers in the array.
    return sum_of_absolute_differences

# We will use a for loop to iterate through the test cases.
for _ in range(int(input())):
    
    # We will use a list to get the input for the test case.
    l = [int(x) for x in input().split()]
    
    # We will use the function to calculate the maximum possible sum
    # of absolute differences between adjacent numbers in the array
    # for a given number of elements and a given sum.
    # We will print the result.
    print(max_sum_of_absolute_differences(l[0], l[1]))