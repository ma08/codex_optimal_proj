

def main():
    expression = input()
    expression = expression.split('+') # split expression by '+'
    result = 0
    for i in expression:
        i = i.split('-') # split expression by '-'
        for j in i:
            result += int(j)
        result -= len(i) - 1 # subtract the number of '-'
    print(result)

main()
