

def main():
    """
    1. Get input (first line is number of test cases, second line is the test cases)
    2. For each test case, if first letter is not equal to second letter, add it to final count
    3. Otherwise, continue (since it's not a distinct letter)
    4. Loop until you reach end of input (i.e. end of string)
    """
    n = int(input()) # number of test cases
    for i in range(n): # for each test case
        s = input() # input string
        count = 0 # reset count
        for i in range(len(s)): # for each letter in string
            if i == (len(s)-1): # if you've reached end of string
                if s[i] != s[i-1]: # if last letter is distinct
                    count += 1 # add to count
                break # exit loop
            if s[i] != s[i+1]: # if first letter is not equal to second letter
                count += 1 # add to count
            else: # otherwise
                continue # continue
        print(count) # print count

if __name__ == "__main__":
    main()
