

def main():
    s = raw_input()
    t = raw_input()
    result = 0
    for i in range(3):
        if s[i] == t[i]:
            result += 1
    print(result)

if __name__ == '__main__':
    main()
