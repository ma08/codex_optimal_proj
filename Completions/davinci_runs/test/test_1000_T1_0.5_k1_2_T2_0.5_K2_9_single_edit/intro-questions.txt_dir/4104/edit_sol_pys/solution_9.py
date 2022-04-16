

def main():
    expression = input()
    expression = expression.split('+')
    result = 0
    for i in expression:
        j = 0
        i = i.split('-')
        for j in i:
            result += int(j)
            j += 1
        if j > 1:
            result -= 1
    print(result)

main()
