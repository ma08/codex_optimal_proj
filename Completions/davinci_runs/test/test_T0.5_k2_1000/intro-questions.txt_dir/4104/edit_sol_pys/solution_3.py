

def main():
    expression = input().split('+') # split the expression by '+'
    result = 0
    for i in expression:
        i = i.split('-') # split the expression by '-'
        for j in i:
            result += int(j)
        result -= len(i) - 1
    print(result)

main()
