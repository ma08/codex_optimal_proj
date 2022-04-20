

def main():
    s = input()
    s = s.replace("A", "").replace("C", "").replace("G", "").replace("T", "")
    print(len(s))

if __name__ == '__main__':
    main()