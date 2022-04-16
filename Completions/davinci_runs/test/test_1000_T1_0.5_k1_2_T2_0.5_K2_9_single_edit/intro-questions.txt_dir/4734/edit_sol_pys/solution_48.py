
def main():
    y, p = input().split(' ')
    if y[-1] == 'e' and y[-2] not in 'aiou':
        print(y + 'x' + ' ' + p)
    elif y[-1] in 'aiou' and y[-2] in 'aiou':
        print(y + 'ex' + ' ' + p)
    else:
        print(y + 'ex' + ' ' + p)

if __name__ == "__main__":
    main()
