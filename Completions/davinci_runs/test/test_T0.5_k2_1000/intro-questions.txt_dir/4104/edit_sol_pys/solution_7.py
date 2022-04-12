

def main():
    expression = input().split('+')  # split expression by '+'
    result = 0
    for i in expression:
        for j in i.split('-'):  # split expression by '-'
            result += int(j)  # add to result
        result -= len(i.split('-')) - 1  # subtract 1 for each '-'
    print(result)

main()
