

def main():
    expression = input()
    expression = expression.split('+')
    result = 0
    for i in expression:
        i = i.split('-')  # i = [1,2,3]
        for j in i:  # j = 1,2,3
            result += int(j)
        result -= len(i) - 1
    print(result)

main()
