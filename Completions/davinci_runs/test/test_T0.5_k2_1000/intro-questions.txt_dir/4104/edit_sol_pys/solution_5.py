

def main():
    expression = input().split('+')  # split the input by '+'
    result = 0
    for i in expression:
        for j in i.split('-'):  # split the input by '-'
            result += int(j)
        result -= len(i.split('-')) - 1
    print(result)

main()
