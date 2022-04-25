

def main():
    expression1 = input()
    expression1 = expression1.split('+') #split the expression by '+'
    result = 0
    for i in expression1: #for each number
        i = i.split('-') #split the number by '-'
        for j in i:
            result += int(j) #add the number to the result
        result -= len(i) - 1 #subtract the number of '-' from the result
    print(result)

main()
