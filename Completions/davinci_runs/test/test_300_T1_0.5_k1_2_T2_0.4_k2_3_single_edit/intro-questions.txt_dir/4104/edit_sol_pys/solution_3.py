def main():
    expression = input().split('+')


    result = 0
    for addend in expression:
        addend = addend.split('-')
        for subtrahend in addend:
            result += int(subtrahend)
        result -= len(addend) - 1

    print(result)

main()
