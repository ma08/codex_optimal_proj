

def main():
    y, p = input().split()
    if y.endswith('ex') and not p.startswith('ex'):
        print(y + p)
    elif y.endswith('e') and not p.startswith('ex'):
        print(y[:-1] + 'x' + p)
    elif y.endswith(('a', 'i', 'o', 'u', 'A', 'I', 'O', 'U')) and not p.startswith('ex'):
    elif y.endswith('ex') and p.startswith('ex'):
        print(y + p[1:])
    elif y.endswith('e') and p.startswith('ex'):
        print(y[:-1] + 'x' + p[1:])
    elif y.endswith(('a', 'i', 'o', 'u', 'A', 'I', 'O', 'U')) and p.startswith('ex'):
        print(y[:-1] + 'ex' + p[1:])
        print(y[:-1] + 'ex' + p)
    else:
        print(y + 'ex' + p)

if __name__ == "__main__":
    main()
