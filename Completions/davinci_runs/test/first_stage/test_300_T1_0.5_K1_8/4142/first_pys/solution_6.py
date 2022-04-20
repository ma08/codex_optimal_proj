

def main():
    s = input()
    odd = ['R', 'U', 'D']
    even = ['L', 'U', 'D']
    for i in range(len(s)):
        if i%2 == 0:
            if not s[i] in odd:
                print("No")
                return
        else:
            if not s[i] in even:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()