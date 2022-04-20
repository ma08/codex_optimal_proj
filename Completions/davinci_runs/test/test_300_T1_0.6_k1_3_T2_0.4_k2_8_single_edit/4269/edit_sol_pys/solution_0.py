

def main():
    s = input()
    p = 0
    for i in s:
        if i == p:
            print("Bad")
            return
        p = i
    print("Good")

if __name__ == '__main__':
    main()
