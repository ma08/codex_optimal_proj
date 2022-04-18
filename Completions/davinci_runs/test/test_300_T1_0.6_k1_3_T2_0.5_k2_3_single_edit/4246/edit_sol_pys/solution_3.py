

def main():
    s = input()[::-1]
    t = input()[::-1]
    result = 0
    for i in range(3):
        if s[i] == t[i]:
            result += 1
    print(result)

if __name__ == '__main__':
    main()
